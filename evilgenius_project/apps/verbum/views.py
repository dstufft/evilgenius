from django.views.generic import ArchiveIndexView

from verbum import conf
from verbum.models import Bloggable

class VerbumIndexView(ArchiveIndexView):

    date_field = "when"
    paginate_by = conf.PAGINATE_BY
    queryset = Bloggable.objects.filter(status=Bloggable.STATUS.published).select_subclasses()