from django.db import models
from django.utils.translation import ugettext_lazy as _


class TimeStampModel(models.Model):

    created = models.DateTimeField(_('Data stworzenia'), auto_now_add=True, db_index=True)
    modified = models.DateTimeField(_('Data modyfikacji'), auto_now=True, db_index=True)

    class Meta:
        abstract = True