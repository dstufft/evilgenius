from django.views.generic import ArchiveIndexView
from verbum.models import Bloggable

class VerbumIndexView(ArchiveIndexView):

    date_field = "when"
    queryset = Bloggable.objects.filter(status=Bloggable.STATUS.published).select_subclasses()