from django.conf.urls.defaults import patterns, url

from verbum.views import VerbumIndexView

urlpatterns = patterns("",
    url(r"^$", VerbumIndexView.as_view(), name="verbum_index"),
)