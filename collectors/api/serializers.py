from cities_light.loading import get_cities_models
from rest_framework import serializers
from rest_framework import fields

Country, Region, City = get_cities_models()


class CountrySerializer(serializers.ModelSerializer):
    """
    Serializer for Country.
    """
    code = fields.CharField(source='code2')

    class Meta:
        model = Country
        fields = (
            'id',
            'name',
            'name_ascii',
            'code',
        )
        
