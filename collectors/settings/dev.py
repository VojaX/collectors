"""Django dev settings for project."""
from .base import *


# general
DEBUG = True
# SITE_ID = SITE_IDS.get('Dev')

# templates
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG
TEMPLATES[0]['OPTIONS']['loaders'] = [
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
]
SECRET_KEY = ''
# static
STATIC_ROOT = ''
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'


