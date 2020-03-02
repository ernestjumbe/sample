from store.settings.base import *
DEBUG = True

database_dir = os.path.join(BASE_DIR, 'databases')

if not os.path.exists(database_dir):
	os.mkdir(database_dir)

media_dir = os.path.join(BASE_DIR, 'media')

if not os.path.exists(media_dir):
	os.mkdir(media_dir)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'store',
        'HOST': 'localhost'
    }
}

# Application definition

INSTALLED_APPS += [
	'debug_toolbar',
	'django_extensions',
]

#==============================================================================
# Static Files
#==============================================================================

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#==============================================================================
# Middleware
#==============================================================================

MIDDLEWARE += [
	'debug_toolbar.middleware.DebugToolbarMiddleware',
]

#==============================================================================
# Miscellaneous project settings
#==============================================================================

#==============================================================================
# Third party app settings
#==============================================================================

#Django Debug Toolbar settings
#=============================

DEBUG_TOOLBAR_PATCH_SETTINGS = False
INTERNAL_IPS = ('127.0.0.1',)

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

# Mail Catcher Email Settings
# ===========================

if DEBUG:
    EMAIL_HOST = '127.0.0.1'
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    EMAIL_PORT = 1025
    EMAIL_USE_TLS = False
