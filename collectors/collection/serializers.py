from rest_framework import serializers
from collectors.api.serializers import CountrySerializer
from . import models

class SetSerializer(serializers.ModelSerializer):
    """
    Serializer for Set
    """
    class Meta:
        model = models.Set
        fields = (
            'id',
            'name',
        )

class CollectionSubTypeSerializer(serializers.ModelSerializer):
    """
    Serializer for CollectionType
    """
    set = SetSerializer()

    class Meta:
        model = models.CollectionSubType
        fields = (
            'id',
            'name',
            'set',
        )

class CollectionTypeSerializer(serializers.ModelSerializer):
    """
    Serializer for CollectionType

    """
    subtype = CollectionSubTypeSerializer()

    class Meta:
        model = models.CollectionType
        fields = (
            'id',
            'name',
            'subtype',
        )

class CategoryTypeSerializer(serializers.ModelSerializer):
    """
    Serializer for CollectionType
    """
    type = CollectionTypeSerializer()

    class Meta:
        model = models.Category
        fields = (
            'id',
            'name',
            'type',
        )

class CollectionListSerializer(serializers.ModelSerializer):
    """
    Serializer for Collection
    """
    category = CategoryTypeSerializer()
    country = CountrySerializer()

    class Meta:
        model = models.Collection
        fields = (
            'id',
            'name',
            'Count',
            'views_no',
            'user_possession',
            'likes',
            'publicated',
            'country',
            'reverse_photo',
            'obverse_photo',
            'description',
            'category',
            'numeration'
        )


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Collection
        fields = (
            'id',
        ) 
