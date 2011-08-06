from django.db import models
from django.utils.translation import ugettext_lazy as _

from verbum.models import Bloggable

class Link(Bloggable):

    url = models.URLField(_("url"), max_length=250)

    class Meta:
        app_label = "verbum"

        verbose_name = _("link")
        verbose_name_plural = _("links")
