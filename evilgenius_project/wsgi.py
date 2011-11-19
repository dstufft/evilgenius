from django.core.handlers.wsgi import WSGIHandler

import pinax.env
import os

raise Exception(os.environ["DJANGO_SETTINGS_MODULE"])

# setup the environment for Django and Pinax
pinax.env.setup_environ(__file__)


# set application for WSGI processing
application = WSGIHandler()
