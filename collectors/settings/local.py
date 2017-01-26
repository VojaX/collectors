# Django local env settings for project.
from .dev import *

# settings will go here
# database
DATABASES['default'].update({
    'NAME': 'collectors',
    'USER': 'postgres',
    'PASSWORD': 'iwko',
    'HOST': '127.0.0.1'
})

LANGUAGES = [
    ('pl', 'Polish'),
    # ('de', 'German'),
    # ('en', 'English'),
    # ('it', 'Italian'),
    # ('es', 'Spanish'),
    # ('fr', 'French'),
    # ('cs', 'Czech'),
]

