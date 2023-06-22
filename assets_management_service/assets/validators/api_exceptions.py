from rest_framework import status
from rest_framework.exceptions import APIException


class TokenRequired(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = {'error': True, 'message': "Token required"}
    default_code = 'token_required'


class InvalidSignature(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = {'error': True, 'message': "Invalid token."}
    default_code = 'invalid_token'


class ExpiredSignature(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = {'error': True, 'message': "Token is expired"}
    default_code = 'not_authenticated'


class InvalidToken(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = {'error': True, 'message': "Invalid token."}
    default_code = 'invalid_token'


class ResourceDoesNotExist(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = {'error': True, 'message': "Resource does not exist."}
    default_code = 'resource_not_exists'


class StandardizedException(APIException):

    def __init__(self, error_status=True, error_obj: object = None,
                 status_code=status.HTTP_400_BAD_REQUEST):
        message = str(error_obj)
        if error_obj is not None:
            try:
                keys = list(error_obj.__dict__.keys())
                if len(keys):
                    message = error_obj.__dict__[keys[0]]
                    if len(message.keys()):
                        message = list(message.keys())[0] + ': ' + message[list(message.keys())[0]][0]
            except Exception:
                message = str(error_obj)
        default_detail = {'error': error_status, 'message': message}
        self.detail = default_detail
        self.default_code = message
        self.status_code = status_code
