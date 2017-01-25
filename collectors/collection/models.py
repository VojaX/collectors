from cities_light.models import Country
from django.db import models
from django.utils.translation import ugettext_lazy as _

from collectors.utils.models import TimeStampModel


class CollectionType(TimeStampModel):
    name = models.CharField(_('Name'), max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created',)
        verbose_name = _('Type')
        verbose_name_plural = _('Types')


class CollectionSubType(TimeStampModel):
    type = models.ForeignKey(CollectionType,
                             verbose_name=_('Type')
                             )
    name = models.CharField(_('Name'), max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created',)
        verbose_name = _('Subtype')
        verbose_name_plural = _('Subtypes')


class Collection(TimeStampModel):
    subtype = models.ForeignKey(CollectionSubType,
                             verbose_name=_('Type')
                             )
    description = models.TextField(_('Description'))
    name = models.CharField(_('Name'), max_length=120)
    set = models.CharField(_('Collection'), max_length=120)
    Count = models.IntegerField(_('Count'))
    views_no = models.IntegerField(_('Views number'))
    user_possession = models.IntegerField(_('User possesses'))
    likes = models.IntegerField(_('Likes number'))
    country = models.ForeignKey(
        Country,
        verbose_name=_('Country'),
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    publicated = models.DateTimeField(_('Publication Date'))
    rewers_photo = models.URLField(_('Rewers photo'))
    awers_photo = models.URLField(_('Awers photo'))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created',)
        verbose_name = _('Colection')
        verbose_name_plural = _('Collections')


