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
SECRET_KEY = 'dmv1%(fam9623l(j#xpga1utxv%xj&o@*0_-e_ev79($#5ua=('
# static
STATIC_ROOT = ''
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'


# # debug-toolbar
# INSTALLED_APPS += (
#     'debug_toolbar',
# )
#
# DEBUG_TOOLBAR_PATCH_SETTINGS = False
# INTERNAL_IPS = ('127.0.0.1', '10.0.2.2',)
# DEBUG_TOOLBAR_CONFIG = {
#     'SHOW_TEMPLATE_CONTEXT': True,
# }
# DEBUG_TOOLBAR_PANELS = [
#     'debug_toolbar.panels.versions.VersionsPanel',
#     'debug_toolbar.panels.timer.TimerPanel',
#     'debug_toolbar.panels.settings.SettingsPanel',
#     'debug_toolbar.panels.headers.HeadersPanel',
#     'debug_toolbar.panels.request.RequestPanel',
#     'debug_toolbar.panels.sql.SQLPanel',
#     'debug_toolbar.panels.staticfiles.StaticFilesPanel',
#     'debug_toolbar.panels.templates.TemplatesPanel',
#     'debug_toolbar.panels.cache.CachePanel',
#     'debug_toolbar.panels.signals.SignalsPanel',
#     'debug_toolbar.panels.logging.LoggingPanel',
#     'debug_toolbar.panels.redirects.RedirectsPanel',
# ]


