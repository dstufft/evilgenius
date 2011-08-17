from django.conf import settings
from django.conf.urls.defaults import patterns, url
from django.core.urlresolvers import reverse
from django.http import Http404

from django.contrib.sites.models import Site
from django.contrib.syndication.views import Feed

from verbum import conf
from verbum.models import Bloggable


class VerbumBaseRSSFeed(Feed):

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


class VerbumBaseAtomFeed(VerbumBaseRSSFeed):

    subtitle = VerbumBaseRSSFeed().description()


class VerbumAllRSSFeed(VerbumBaseRSSFeed):
    pass


class VerbumAllAtomFeed(VerbumBaseAtomFeed):
    pass


class VerbumCategoryRSSFeed(VerbumBaseRSSFeed):

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


class VerbumCategoryAtomFeed(VerbumCategoryRSSFeed, VerbumBaseAtomFeed):
    pass

urlpatterns = patterns("",
    url("^all/rss/$", VerbumAllRSSFeed()),
    url("^all/atom/$", VerbumAllAtomFeed()),

    url("^category/(?P<category>[\w]+)/rss/$", VerbumCategoryRSSFeed()),
    url("^category/(?P<category>[\w]+)/atom/$", VerbumCategoryAtomFeed()),
)
