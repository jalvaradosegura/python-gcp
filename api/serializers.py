from rest_framework import serializers

from .models import Drug, Vaccination
from .rut_validator import rut_validator


class DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = ('id', 'name', 'code', 'description', 'vaccinations')
        extra_kwargs = {'vaccinations': {'required': False}}


class VaccinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccination
        fields = ('id', 'rut', 'dose', 'date', 'drug')

    def validate_rut(self, value):
        valid_rut = rut_validator(value)
        if valid_rut is False:
            raise serializers.ValidationError("Please enter a valid rut")
        return value.replace('-', '').replace('.', '')
