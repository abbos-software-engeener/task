from rest_framework import serializers

from . import models
from .models import  Country, Town


class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name', 'title', 'month', 'status')


class TownSerializers(serializers.ModelSerializer):
    class Meta:
        model = Town
        fields = '__all__'







