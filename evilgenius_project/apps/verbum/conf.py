from django.conf import settings
from django.utils.translation import ugettext as _


PAGINATE_BY = getattr(settings, "VERBUM_PAGINATE_BY", 10)

CATEGORIES = getattr(settings, "VERBUM_CATEGORIES", [
    ("post", _("Post")),
    ("link", _("Link")),
])