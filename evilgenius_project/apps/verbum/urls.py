from django.conf.urls.defaults import patterns, url

from verbum.views import VerbumIndexView, VerbumDetailView

urlpatterns = patterns("",
    url(r"^$", VerbumIndexView.as_view(), name="verbum_index"),
    url(r"^page(?P<page>[\d]+)/$", VerbumIndexView.as_view(), name="verbum_index_paged"),

    url(
        r"^(?P<year>[0-9]{4})/(?P<month>[\w]{3})/(?P<day>[0-3][0-9])/(?P<slug>[-\w]+)/$",
        VerbumDetailView.as_view(),
        name="verbum_detail"
    ),
)