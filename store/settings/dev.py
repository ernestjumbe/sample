from store.settings.base import *  # pylint: disable=W291,E202

DEBUG = True
TEMPLATE_DEBUG = True

VAR_ROOT = '/var/www/store.com'
MEDIA_ROOT = os.path.join(VAR_ROOT, 'uploads')
STATIC_ROOT = os.path.join(VAR_ROOT, 'static')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'store',
        'USER': '',
        'PASSWORD': '',
        'PORT': '',
        'HOST': '',
    }
}

# WSGI_APPLICATION = 'store.wsgi.dev.application'
