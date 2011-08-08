from django.views.generic import ArchiveIndexView, DateDetailView

from verbum import conf
from verbum.models import Bloggable

class VerbumIndexView(ArchiveIndexView):

    date_field = "when"
    paginate_by = conf.PAGINATE_BY
    
    queryset = Bloggable.objects.filter(status=Bloggable.STATUS.published).select_subclasses()


class CategoryIndexView(VerbumIndexView):

    template_name = "verbum/bloggable_categories.html"

    def get_context_data(self, **kwargs):
        context = super(CategoryIndexView, self).get_context_data(**kwargs)
        context.update({
            "category": self.kwargs["category"],
        })
        return context

    def get_queryset(self):
        qs = super(CategoryIndexView, self).get_queryset()
        return qs.filter(category=getattr(Bloggable.CATEGORIES, self.kwargs["category"]))

class VerbumDetailView(DateDetailView):

    date_field = "when"
    queryset = Bloggable.objects.filter(status=Bloggable.STATUS.published).select_subclasses()

    def get_template_names(self):
        template_names = ["verbum/%s/detail.html" % self.object._meta.module_name]
        template_names.extend(
            super(VerbumDetailView, self).get_template_names()
        )
        return template_names