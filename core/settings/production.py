import environ

from .base import *  # noqa: F403

DEBUG = False

env = environ.Env()

HOST_NAME = env('HOST_NAME')
ALLOWED_HOSTS = [
    HOST_NAME,
]
CORS_ALLOWED_ORIGINS = [
    f'https://{HOST_NAME}',
]

DATABASES = {
    # read os.environ['DATABASE_URL'] and raises
    # ImproperlyConfigured exception if not found
    # The db() method is an alias for db_url().
    'default': env.db(),
}
DATABASES['default']['CONN_MAX_AGE'] = env.int('CONN_MAX_AGE', default=60)


# Staticfiles
# https://whitenoise.readthedocs.io/en/latest/django.html

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # noqa: F405

STORAGES = {
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedManifestStaticFilesStorage',
    },
}
