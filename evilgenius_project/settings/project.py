import os.path
import posixpath

from .base import PROJECT_ROOT
from .pinax import STATICFILES_DIRS, TEMPLATE_DIRS, INSTALLED_APPS, TEMPLATE_CONTEXT_PROCESSORS

TEMPLATE_WIREFRAME = False

ADMINS = [
    ("Donald Stufft", "donald@e.vilgeni.us"),
]

MANAGERS = ADMINS

INTERNAL_IPS = [
    "127.0.0.1",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "e.vilgeni.us",
    }
}

TIME_ZONE = "US/Eastern"
LANGUAGE_CODE = "en-us"

USE_I18N = True
USE_L10N = True

MEDIA_ROOT = os.path.join(PROJECT_ROOT, "site_media", "media")
MEDIA_URL = "/site_media/media/"

STATIC_ROOT = os.path.join(PROJECT_ROOT, "site_media", "static")
STATIC_URL = "/site_media/static/"

STATICFILES_DIRS = [os.path.join(PROJECT_ROOT, "static")] + STATICFILES_DIRS

ADMIN_MEDIA_PREFIX = posixpath.join(STATIC_URL, "admin/")

ROOT_URLCONF = "evilgenius_project.urls"

TEMPLATE_CONTEXT_PROCESSORS += ["evilgenius.context_processors.configuration"]

TEMPLATE_DIRS = [os.path.join(PROJECT_ROOT, "templates")] + TEMPLATE_DIRS

FIXTURE_DIRS = [
    os.path.join(PROJECT_ROOT, "fixtures"),
]

INSTALLED_APPS += [
    "verbum",
    "verbum.posts",
    "verbum.links",
]

CONTACT_EMAIL = "donald@e.vilgeni.us"
TWITTER_URL = "http://twitter.com/dstufft"

DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
}