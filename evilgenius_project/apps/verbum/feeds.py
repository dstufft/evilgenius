from django.conf import settings
from django.conf.urls.defaults import patterns, url
from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.utils.feedgenerator import Atom1Feed

from django.contrib.sites.models import Site
from django.contrib.syndication.views import Feed

from taggit.models import Tag

from verbum import conf
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

    feed_type = Atom1Feed
    subtitle = VerbumAllRSSFeed().description()


class VerbumCategoryRSSFeed(VerbumAllRSSFeed):

    def get_object(self, request, category):
        cat_items = [x for x in conf.CATEGORIES if x[0] == category]
        if len(cat_items):
            return cat_items[0]
        else:
            raise Http404("Feed for Category: %s Not Found" % category)

    def title(self, obj):
        return "%s: %s" % (Site.objects.get_current().name, obj[1])

    def link(self, obj):
        return reverse("verbum_category", kwargs={"category": obj[0]})

    def items(self, obj):
        return Bloggable.objects.select_subclasses().filter(category=getattr(Bloggable.CATEGORIES, obj[0]))


class VerbumCategoryAtomFeed(VerbumCategoryRSSFeed):

    feed_type = Atom1Feed
    subtitle = VerbumCategoryRSSFeed().description()


class VerbumTagRSSFeed(VerbumAllRSSFeed):

    def get_object(self, request, tag):
        return get_object_or_404(Tag, name=tag)

    def title(self, obj):
        return "%s: %s" % (Site.objects.get_current().name, obj.name)

    def link(self, obj):
        return reverse("verbum_tag", kwargs={"tag": obj.name})

    def items(self, obj):
        return Bloggable.objects.select_subclasses().filter(tags=obj)


class VerbumTagAtomFeed(VerbumTagRSSFeed):

    feed_type = Atom1Feed
    subtitle = VerbumTagRSSFeed().description()

urlpatterns = patterns("",
    url("^all/rss/$", VerbumAllRSSFeed()),
    url("^all/atom/$", VerbumAllAtomFeed()),

    url("^category/(?P<category>[\w]+)/rss/$", VerbumCategoryRSSFeed()),
    url("^category/(?P<category>[\w]+)/atom/$", VerbumCategoryAtomFeed()),

    url("^tag/(?P<tag>[\w]+)/rss/$", VerbumTagRSSFeed()),
    url("^tag/(?P<tag>[\w]+)/atom/$", VerbumTagAtomFeed()),
)
