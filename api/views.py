from rest_framework import generics, status
from rest_framework.parsers import JSONParser

from .models import Drug, Vaccination
from .serializers import DrugSerializer, VaccinationSerializer
from .custom_exception import CustomValidation


class DrugList(generics.ListAPIView):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer


class DrugDetail(generics.RetrieveAPIView):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer
    lookup_field = 'id'


class DrugPost(generics.CreateAPIView):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer
    parser_classes = [JSONParser]


class DrugPutDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer
    lookup_field = 'id'

    def get_object(self):
        obj = super().get_object()
        if self.request.method == 'DELETE':
            if obj.vaccinations.count() > 0:
                raise CustomValidation(
                    'The drug has associated vaccinations',
                    'vaccinations',
                    status_code=status.HTTP_400_BAD_REQUEST
                )
        return obj


class VaccinationListCreate(generics.ListCreateAPIView):
    queryset = Vaccination.objects.all()
    serializer_class = VaccinationSerializer


class VaccinationDetailPutDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vaccination.objects.all()
    serializer_class = VaccinationSerializer
    lookup_field = 'id'
    parser_classes = [JSONParser]
