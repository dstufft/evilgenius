from django.conf import settings


PAGINATE_BY = getattr(settings, "VERBUM_PAGINATE_BY", 10)