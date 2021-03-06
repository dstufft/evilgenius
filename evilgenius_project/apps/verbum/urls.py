from django.conf.urls.defaults import patterns, url

from verbum.views import VerbumIndexView, CategoryIndexView, TagIndexView, VerbumDetailView

urlpatterns = patterns("",
    url(r"^(?:page(?P<page>[\d]+)/)?$", VerbumIndexView.as_view(), name="verbum_index"),
    url(r"^category/(?P<category>[\w]+)/(?:page(?P<page>[\d]+)/)?$", CategoryIndexView.as_view(), name="verbum_category"),
    url(r"^tag/(?P<tag>[\w]+)/(?:page(?P<page>[\d]+)/)?$", TagIndexView.as_view(), name="verbum_tag"),

    url(
        r"^(?P<year>[0-9]{4})/(?P<month>[\w]{3})/(?P<day>[0-3][0-9])/(?P<slug>[-\w]+)/$",
        VerbumDetailView.as_view(),
        name="verbum_detail"
    ),
)