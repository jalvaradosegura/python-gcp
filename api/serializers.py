from rest_framework import serializers

from .models import Drug, Vaccination


class DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = ('id', 'name', 'code', 'description', 'vaccinations')
        extra_kwargs = {'vaccinations': {'required': False}}


class VaccinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccination
        fields = ('id', 'rut', 'dose', 'date', 'drug')
