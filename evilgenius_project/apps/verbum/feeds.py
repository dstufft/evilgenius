from django.conf import settings
from django.conf.urls.defaults import patterns, url
from django.core.urlresolvers import reverse

from django.contrib.sites.models import Site
from django.contrib.syndication.views import Feed

from verbum.models import Bloggable


class VerbumAllRSSFeed(Feed):

    def title(self):
        return getattr(settings, "VERBUM_BLOG_NAME", Site.objects.get_current().name)

    def link(self):
        return getattr(settings, "VERBUM_BLOG_LINK", reverse("verbum_index"))

    def description(self):
        return getattr(settings, "VERBUM_BLOG_DESCRIPTION", "A Verbum Blog")

    def items(self):
        return Bloggable.objects.select_subclasses()

    def item_title(self, item):
        return item.get_title()

    def item_description(self, item):
        return item.get_summary()

    def item_author_name(self, item):
        return item.author.get_full_name() if item.author.get_full_name() else unicode(item.author)

    def item_author_email(self, item):
        return item.author.email

    def item_pubdate(self, item):
        return item.when

    def item_categories(self, item):
        return [x.name for x in item.tags.all()]


class VerbumAllAtomFeed(VerbumAllRSSFeed):

    subtitle = VerbumAllRSSFeed().description()

urlpatterns = patterns("",
    url("^all/rss/$", VerbumAllRSSFeed()),
    url("^all/atom/$", VerbumAllAtomFeed()),
)
