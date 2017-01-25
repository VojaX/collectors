from cities_light.models import Country
from django.db import models
from django.utils.translation import ugettext_lazy as _

from collectors.utils.models import TimeStampModel


class Category(TimeStampModel):
    name = models.CharField(_('Name'), max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created',)
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


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
    category = models.ForeignKey(Category,
                                 verbose_name=_('Category')
                                 )
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
    reverse_photo = models.URLField(_('Reverse photo'))
    obverse_photo = models.URLField(_('Obverse photo'))
    numeration = models.CharField(_('Numeration'), max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created',)
        verbose_name = _('Colection')
        verbose_name_plural = _('Collections')
