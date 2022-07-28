from rest_framework.exceptions import APIException
from rest_framework.views import status

class UniqueException(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = 'This value must be unique.'


class NotFoundException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = 'Not found.'

class ValueException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Review your values"