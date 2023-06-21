from rest_framework.response import Response
from rest_framework import status as rest_status


class BaseResponse:

    @staticmethod
    def response_message(status, data, message=''):
        if status == "success":
            if len(data) == 0:
                message = "No records found"
            return Response(
                {"status": status, "status_code": rest_status.HTTP_200_OK, "message": message, "data": data})
        elif status == "error":
            data = str(data).replace(" matching query", "")
            return Response({"status": "error", "message": message, "data": data})
        if status == "deleted":
            return Response(
                {"status": status, "status_code": rest_status.HTTP_200_OK, "message": message, "data": data})
        elif status == rest_status.HTTP_404_NOT_FOUND:
            return Response(
                {"status": "success", "status_code": rest_status.HTTP_404_NOT_FOUND, "message": message, "data": data})

    @staticmethod
    def response(status, data, code, message=''):
        if status == "success":
            if len(data) == 0:
                message = "No records found"
            return Response({"status": status, "status_code": code, "message": message, "data": data})
        elif status == "error":
            data = str(data).replace(" matching query", "")
            return Response({"status": "error", "message": message, "data": data})
        if status == "deleted":
            return Response(
                {"status": status, "status_code": code, "message": message, "data": data})
        elif status == rest_status.HTTP_404_NOT_FOUND:
            return Response(
                {"status": "success", "status_code": code, "message": message, "data": data})
