# Django local env settings for project.
from .dev import *


DATABASES['default'].update({
    'NAME': '',
    'USER': '',
    'PASSWORD': '',
    'HOST': '127.0.0.1'
})



