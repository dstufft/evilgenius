from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()


handler500 = "pinax.views.server_error"


urlpatterns = patterns("",
    url(r"^admin/", include(admin.site.urls)),

    #url(r"about/dstufft/", TemplateView.as_view(template_name="about/dstufft.html")),
    url(r"", include("verbum.urls")),
)


if settings.SERVE_MEDIA:
    urlpatterns += patterns("",
        url(r"", include("staticfiles.urls")),
    )
