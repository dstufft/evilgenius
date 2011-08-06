from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils import Choices
from model_utils.fields import StatusField
from model_utils.managers import InheritanceManager

class Bloggable(models.Model):

    STATUS = Choices(
        ("draft", _("draft")),
        ("published", _("published")),
    )

    # Meta Data
    status = StatusField(_("status"))
    when = models.DateTimeField(_("when"), default=datetime.now)

    # Common Data
    title = models.CharField(_("title"), max_length=150)
    slug = models.SlugField(_("slug"), max_length=250, unique_for_date="when")
    author = models.ForeignKey("auth.User", verbose_name=_("author"))

    objects = InheritanceManager()

    class Meta:
        verbose_name = _("bloggable")
        verbose_name_plural = _("bloggables")

        ordering = ["when", "title"]

    def __unicode__(self):
        return "{0}".format(self.title)
