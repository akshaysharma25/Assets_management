from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from rest_framework import status
from assets.utils.response.constants import EX

class Util:

    def valid_url(self, to_validate: str) -> bool:
        validator = URLValidator()
        print(to_validate)
        try:
            validator(to_validate)
            print(True)
            return True
        except ValidationError as exception:
            print(exception)
            return False

    def is_valid_url(self, url):
        import re
        regex = re.compile(
            r'^https?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return url is not None and regex.search(url)

    def validate_latitude(self, latitude):
        import re
        regex = re.compile('^(\+|-)?((\d((\.)|\.\d{1,6})?)|(0*?[0-8]\d((\.)|\.\d{1,6})?)|(0*?90((\.)|\.0{1,6})?))$')
        return latitude is not None and regex.search(latitude)

    def validate_longitude(self, longitude):
        import re
        regex = re.compile(
            '^(\+|-)?((\d((\.)|\.\d{1,6})?)|(0*?\d\d((\.)|\.\d{1,6})?)|(0*?1[0-7]\d((\.)|\.\d{1,6})?)|(0*?180((\.)|\.0{1,6})?))$')
        return longitude is not None and regex.search(longitude)

    def get_exception_message(self, exception):
        error_data = exception.args[0]
        error = error_data.get("message", "Something went wrong. Try again.") if type(
            error_data) == 'dict' else str(exception)
        return {"message": EX, "status": "BAD_REQUEST", "error": error, "status_code": status.HTTP_400_BAD_REQUEST}

    def get_error_message(self, exception, error_msg):
        error_data = exception.args[0]
        error = error_data.get("message", error_msg) if type(
            error_data) == 'dict' else str(exception)
        return {"message": EX, "status": "BAD_REQUEST", "error": error, "status_code": status.HTTP_400_BAD_REQUEST}

    def get_error_message(self, error_msg):
        return {"message": EX, "status": "BAD_REQUEST", "error": error_msg, "status_code": status.HTTP_400_BAD_REQUEST}

    def get_validation_message(self, message, error_message_list):
        return {"message": message, "status": "BAD_REQUEST", "status_code": status.HTTP_400_BAD_REQUEST,
                "error": error_message_list}

    def get_created_message(self, message):
        return {"message": message, "status": 'CREATED', "status_code": status.HTTP_201_CREATED}

    def get_created_message_withData(self, message, data):
        return {"message": message, "status": 'CREATED', "status_code": status.HTTP_201_CREATED, "data": data}

    def get_fetch_message(self, message, data):
        return {"message": message, "status": 'OK', "status_code": status.HTTP_200_OK, "data": data}

    def get_updated_message(self, message):
        return {"message": message, "status": 'UPDATED', "status_code": status.HTTP_204_NO_CONTENT}

    def get_deleted_message(self, message, data):
        return {"message": message, "status": 'DELETED', "status_code": status.HTTP_204_NO_CONTENT, "data": data}

    def get_no_record_message(self, message):
        return {"message": message, "status": 'OK',"status_code": status.HTTP_204_NO_CONTENT}

    def get_param_object(self, params, key):
        """Utility function to pop object from params based on the provided key.
        If key is not present empty string is returned"""
        data = params.pop(key) if params.get(key) else ""
        return data
