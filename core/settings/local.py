import socket

import environ

from .base import *  # noqa: F403

DEBUG = True

env = environ.Env()

HOST_NAME = env('HOST_NAME')
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    HOST_NAME,
]
CORS_ALLOWED_ORIGINS = [
    'http://localhost',
    'http://127.0.0.1',
    f'http://{HOST_NAME}',
]


INSTALLED_APPS += [  # noqa: F405
    'debug_toolbar',
]


MIDDLEWARE += [  # noqa: F405
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]


# django-debug-toolbar
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[: ip.rfind('.')] + '.1' for ip in ips] + ['127.0.0.1', '10.0.2.2']


# Database
DATABASES = {
    'default': {
        'ENGINE': env('DATABASE_ENGINE'),
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'PORT': env('DATABASE_PORT'),
    }
}


# Staticfiles
# https://whitenoise.readthedocs.io/en/latest/django.html

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # noqa: F405

STORAGES = {
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
    },
}
