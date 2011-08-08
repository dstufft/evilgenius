from django.views.generic import ArchiveIndexView, DateDetailView

from verbum import conf
from verbum.models import Bloggable

class VerbumIndexView(ArchiveIndexView):

    date_field = "when"
    paginate_by = conf.PAGINATE_BY
    queryset = Bloggable.objects.filter(status=Bloggable.STATUS.published).select_subclasses()

class VerbumDetailView(DateDetailView):

    date_field = "when"
    queryset = Bloggable.objects.filter(status=Bloggable.STATUS.published).select_subclasses()

    def get_template_names(self):
        template_names = ["verbum/%s/detail.html" % self.object._meta.module_name]
        template_names.extend(
            super(VerbumDetailView, self).get_template_names()
        )
        return template_names