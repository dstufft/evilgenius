from django.db import models
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from verbum.models import Bloggable

class Link(Bloggable):

    url = models.URLField(_("url"), max_length=250)
    summary = models.TextField(_("summary"), blank=True)

    class Meta:
        app_label = "verbum"

        verbose_name = _("link")
        verbose_name_plural = _("links")

    def get_absolute_url(self):
        return self.url

    def get_summary(self):
        return render_to_string("verbum/links/summary.html", {
            "link": self,
        })
