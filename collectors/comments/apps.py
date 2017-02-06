from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CommentsConfig(AppConfig):
    name = 'collectors.comments'
    verbose_name = _('Comments')