from .base import *

from .django import *

from .pinax import *

from .project import *

# This is Crappy, but It keeps secret settings out of the repository
from .secret import *

from .gondor import *

try:
    from .local import *
except ImportError:
    pass