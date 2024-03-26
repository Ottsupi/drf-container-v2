import environ

from .base import *  # noqa: F403

DEBUG = False

env = environ.Env()

ALLOWED_HOSTS = [env('HOST_NAME')]
CORS_ALLOWED_ORIGINS = [env('HOST_NAME')]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'PORT': env('DATABASE_PORT'),
    }
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
