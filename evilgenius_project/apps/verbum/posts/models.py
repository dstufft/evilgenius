from django.db import models
from django.utils.translation import ugettext_lazy as _

from verbum.models import Bloggable

class Post(Bloggable):

    body = models.TextField(_("body"))
    excerpt = models.TextField(_("excerpt"), blank=True)

    class Meta:
        app_label = "verbum"
        
        verbose_name = _("post")
        verbose_name_plural = _("posts")

    def get_summary(self):
        return self.excerpt