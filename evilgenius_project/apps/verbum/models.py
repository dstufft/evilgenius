from datetime import datetime

from django.core.urlresolvers import reverse
from django.db import models
from django.template.loader import render_to_string
from django.utils.html import escape
from django.utils.translation import ugettext_lazy as _

from model_utils import Choices
from model_utils.fields import StatusField, SplitField, SPLIT_MARKER, SPLIT_DEFAULT_PARAGRAPHS
from model_utils.managers import InheritanceManager

from taggit.managers import TaggableManager

from verbum import conf

class Bloggable(models.Model):

    category_name = ""

    STATUS = Choices(
        ("draft", _("draft")),
        ("published", _("published")),
    )

    CATEGORIES = Choices(*conf.CATEGORIES)

    # Meta Data
    status = StatusField(_("status"))
    when = models.DateTimeField(_("when"), default=datetime.now)
    allow_comments = models.BooleanField(_("Allow Comments"), default=True)
    category = models.CharField(_("category"), max_length=75, choices=CATEGORIES, editable=False)

    # Common Data
    title = models.CharField(_("title"), max_length=150)
    slug = models.SlugField(_("slug"), max_length=250, unique_for_date="when")
    author = models.ForeignKey("auth.User", verbose_name=_("author"))

    objects = InheritanceManager()
    tags = TaggableManager(blank=True)

    class Meta:
        verbose_name = _("bloggable")
        verbose_name_plural = _("bloggables")

        ordering = ["when", "title"]

    def __unicode__(self):
        return "{0}".format(self.title)

    def save(self, *args, **kwargs):
        if not len(self.category) and self.category_name:
            self.category = getattr(self.CATEGORIES, self.category_name)
        return super(Bloggable, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "verbum_detail",
            kwargs={
                "year": self.when.strftime("%Y"),
                "month": self.when.strftime("%b").lower(),
                "day": self.when.strftime("%d"),
                "slug": self.slug,
            }
        )

    def get_title(self):
        return self.title


class Post(Bloggable):

    category_name = "post"

    body = SplitField(_("body"),
        help_text=_("Will split the excerpt at %s paragraphs, or when it finds %s") % \
                  (SPLIT_DEFAULT_PARAGRAPHS, escape(SPLIT_MARKER)))

    class Meta:
        verbose_name = _("post")
        verbose_name_plural = _("posts")

    def get_summary(self):
        return render_to_string("verbum/post/summary.html", {
            "post": self,
        })


class Link(Bloggable):

    category_name = "link"

    url = models.URLField(_("url"), max_length=250)
    summary = models.TextField(_("summary"), blank=True)

    class Meta:
        verbose_name = _("link")
        verbose_name_plural = _("links")

    def get_absolute_url(self):
        return self.url

    def get_summary(self):
        return render_to_string("verbum/link/summary.html", {
            "link": self,
        })
