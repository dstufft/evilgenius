import os.path

from .base import DEBUG, PINAX_ROOT
from .django import (
    STATICFILES_FINDERS,
    MIDDLEWARE_CLASSES,
    TEMPLATE_DIRS,
    TEMPLATE_CONTEXT_PROCESSORS,
    INSTALLED_APPS
)

PINAX_THEME = "default"

SERVE_MEDIA = DEBUG

COMPRESS = False
COMPRESS_OUTPUT_DIR = "cache"

STATICFILES_DIRS = [
    os.path.join(PINAX_ROOT, "themes", PINAX_THEME, "static"),
]

STATICFILES_FINDERS += ["compressor.finders.CompressorFinder"]

MIDDLEWARE_CLASSES += [
    "pinax.middleware.security.HideSensistiveFieldsMiddleware",
]

TEMPLATE_DIRS = [os.path.join(PINAX_ROOT, "themes", PINAX_THEME, "templates")] + TEMPLATE_DIRS

TEMPLATE_CONTEXT_PROCESSORS += [
    "staticfiles.context_processors.static",
    "pinax.core.context_processors.pinax_settings",
]

INSTALLED_APPS += [
    "pinax.templatetags",

    # external
    "staticfiles",
    "compressor",
    "analytics",
]