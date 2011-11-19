from importlib import import_module
import sys

from .base import *

from .django import *

from .pinax import *

from .project import *

try:
    from local_settings import *

    try:
        mod = import_module(".{0}".format(GONDOR_INSTANCE), package="evilgenius_project.settings")
        current_module = sys.modules[__name__]
        for attr in dir(mod):
            if attr == attr.upper():
                setattr(current_module, attr, getattr(mod, attr))
    except ImportError:
        pass
except ImportError:
    pass
