import jwt
from rest_framework.permissions import BasePermission
from assets.utils.logger import service_logger

from assets.validators.api_exceptions import TokenRequired, InvalidSignature, ExpiredSignature, InvalidToken
from assets.validators.token_validator import token_validator


class PermissionChecker(BasePermission):
    def has_permission(self, request, view):
        auth_header = request.headers.get('Authorization', None)
        if auth_header is not None:
            try:
                decoded_token = token_validator(token=auth_header)
                role = decoded_token['role']
                username = decoded_token['name']
                # tenant_id = decoded_token['tenantid']
                return True
            except jwt.InvalidSignatureError as e:
                service_logger.error(e)
                raise InvalidSignature()
            except jwt.ExpiredSignatureError as e:
                service_logger.error(e)
                raise ExpiredSignature()
            except Exception as e:
                service_logger.error(e)
                raise InvalidToken()
        else:
            raise TokenRequired()
