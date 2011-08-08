from django.conf.urls.defaults import patterns, url

from verbum.views import VerbumIndexView, CategoryIndexView, VerbumDetailView

urlpatterns = patterns("",
    # General Archive Views
    url(r"^$", VerbumIndexView.as_view(), name="verbum_index"),
    url(r"^page(?P<page>[\d]+)/$", VerbumIndexView.as_view(), name="verbum_index_paged"),

    # Category Archive Views
    url(r"^category/(?P<category>[\w]+)/$", CategoryIndexView.as_view(), name="verbum_category_index"),

    url(
        r"^(?P<year>[0-9]{4})/(?P<month>[\w]{3})/(?P<day>[0-3][0-9])/(?P<slug>[-\w]+)/$",
        VerbumDetailView.as_view(),
        name="verbum_detail"
    ),
)