from django.utils.encoding import force_text

from rest_framework.exceptions import APIException
from rest_framework import status
import jwt


class CustomValidation(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = 'A server error occurred.'

    def __init__(self, detail, field, status_code):
        if status_code is not None:
            self.status_code = status_code
        if detail is not None:
            self.detail = {field: force_text(detail)}
        else:
            self.detail = {'detail': force_text(self.default_detail)}


def validate_jwt_token(request):
    token = request.META.get('HTTP_AUTHORIZATION', '').replace('Bearer ', '')
    try:
        jwt.decode(token, 'secret', algorithms=['HS256'])
    except:
        raise CustomValidation(
                'Invalid token',
                'token',
                status_code=status.HTTP_403_FORBIDDEN
            )
