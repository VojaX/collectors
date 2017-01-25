from rest_framework import serializers

from collectors.api.serializers import CountrySerializer
from . import models

class CollectionTypeSerializer(serializers.ModelSerializer):
    """
    Serializer for CollectionType
    """
    class Meta:
        model = models.CollectionType
        fields = (
            'id',
            'name',
        )


class CollectionSubTypeSerializer(serializers.ModelSerializer):
    """
    Serializer for CollectionType
    """
    type = CollectionTypeSerializer()
    class Meta:
        model = models.CollectionSubType
        fields = (
            'id',
            'name',
            'type',
        )


class CollectionListSerializer(serializers.ModelSerializer):
    """
    Serializer for Collection
    """
    subtype = CollectionSubTypeSerializer()
    country = CountrySerializer()

    class Meta:
        model = models.Collection
        fields = (
            'id',
            'name',
            'set',
            'Count',
            'views_no',
            'user_possession',
            'likes',
            'publicated',
            'country',
            'rewers_photo',
            'awers_photo',
            'subtype',
            'description',
        )