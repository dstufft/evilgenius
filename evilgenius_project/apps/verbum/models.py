from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

class Bloggable(models.Model):

    STATUS_DRAFT = 0
    STATUS_PENDING_REVIEW = 1
    STATUS_PUBLISHED = 2

    STATUS_CHOICES = [
        (STATUS_DRAFT, _("draft")),
        (STATUS_PENDING_REVIEW, _("pending review")),
        (STATUS_PUBLISHED, _("published"))
    ]

    VISIBILITY_PUBLIC = 0
    VISIBILITY_PASSWORD_PROTECTED = 1
    VISIBILITY_PRIVATE = 2

    VISIBILITY_CHOICES = [
        (VISIBILITY_PUBLIC, _("public")),
        (VISIBILITY_PASSWORD_PROTECTED, _("password protected")),
        (VISIBILITY_PRIVATE, _("private"))
    ]

    # Meta Data
    status = models.PositiveIntegerField(_("status"), choices=STATUS_CHOICES)
    visibility = models.PositiveIntegerField(_("visibility"), choices=VISIBILITY_CHOICES)
    publish_on = models.DateTimeField(_("publish date"), default=datetime.now)

    # Optional Meta Data (Based on Visibility)
    sticky = models.BooleanField(_("sticky"))
    password = models.CharField(_("password"), max_length=150, blank=True)

    # Common Data
    title = models.CharField(_("title"), max_length=150)
    slug = models.SlugField(_("slug"), max_length=250, unique_for_date="publish_on")
    author = models.ForeignKey("auth.User", verbose_name=_("author"))

    class Meta:
        verbose_name = _("bloggable")
        verbose_name_plural = _("bloggables")

        ordering = ["publish_on", "title"]

    def __unicode__(self):
        return u"{0}".format(self.title)