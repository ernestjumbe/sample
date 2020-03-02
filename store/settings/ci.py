from store.settings.base import *  # pylint: disable=W291,E202
from store.settings.secrets import *

DEBUG = True
TEMPLATE_DEBUG = True

VAR_ROOT = '/var/www/store.com'
MEDIA_ROOT = os.path.join(VAR_ROOT, 'uploads')
STATIC_ROOT = os.path.join(VAR_ROOT, 'static')

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'storetest',
        'USER': 'postgres',
        #'PASSWORD': 'db_password',
        #'PORT': 'port',
        #'HOST': 'localhost',
    }
}

# WSGI_APPLICATION = 'store.wsgi.dev.application'
