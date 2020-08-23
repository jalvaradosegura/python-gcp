import uuid

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
import jwt

from .models import Drug, Vaccination
from .serializers import DrugSerializer, VaccinationSerializer
from .custom_validations import CustomValidation, validate_jwt_token


class DrugList(generics.ListAPIView):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer

    def get(self, request, *args, **kwargs):
        validate_jwt_token(self.request)
        return super().get(request, *args, **kwargs)


class DrugDetail(generics.RetrieveAPIView):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        validate_jwt_token(self.request)
        return super().get(request, *args, **kwargs)


class DrugPost(generics.CreateAPIView):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer
    parser_classes = [JSONParser]

    def create(self, request, *args, **kwargs):
        validate_jwt_token(self.request)
        return super().create(request, *args, **kwargs)


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

    def delete(self, request, *args, **kwargs):
        validate_jwt_token(self.request)
        return super().delete(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        validate_jwt_token(self.request)
        return super().put(request, *args, **kwargs)


class VaccinationListCreate(generics.ListCreateAPIView):
    queryset = Vaccination.objects.all()
    serializer_class = VaccinationSerializer

    def get(self, request, *args, **kwargs):
        validate_jwt_token(self.request)
        return super().get(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        validate_jwt_token(self.request)
        return super().create(request, *args, **kwargs)


class VaccinationDetailPutDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vaccination.objects.all()
    serializer_class = VaccinationSerializer
    lookup_field = 'id'
    parser_classes = [JSONParser]

    def get(self, request, *args, **kwargs):
        validate_jwt_token(self.request)
        return super().get(request, *args, **kwargs)


class GetToken(generics.GenericAPIView):
    def get(self, request):
        token = jwt.encode(
            {'some': str(uuid.uuid4())}, 'secret', algorithm='HS256'
        )
        return Response({'token': token}, status.HTTP_200_OK)
