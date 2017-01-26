from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CollectionConfig(AppConfig):
    name = 'collectors.collection'
    verbose_name = _('Collections')