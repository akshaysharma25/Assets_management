from rest_framework.viewsets import ViewSet
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from assets.utils.response.constants import *
from assets.utils.response.base_response import *
from django.db.models import Q
from django_filters.utils import timezone
from assets.utils.logger import service_logger
from assets.models.assets import AssetRequestModel



class AssetServices(ViewSet, ModelViewSet):

    # ==================== CONSTRUCTOR STARTS ===================
    def __init__(self, *args, **kwargs):
        print("Asset Service Initialized")

    # ==================== CONSTRUCTOR ENDS =====================

    # ==================== SERVICE METHODS START ================

    def create_asset_request(self, params):
        try:
            queryset = AssetRequestModel.objects.create(
                request_id=params.data['request_id'],
                asset_id=params.data['asset_id'],
                student_id=params.data['student_id'],  # Get this from user management
                asset_type_id=params.data['asset_type_id'],
                asset_type_lable=params.data['asset_type_lable'],
                quantity=params.data['quantity'],
                description=params.data['description'],
                asset_request_title=params.data['asset_request_title'],
                request_data=params.data['request_data'],
                expected_return_date=params.data['expected_return_date'],
                purpose_of_request=params.data['purpose_of_request'],
                delivery_info=params.data['delivery_info'],
            )
            queryset.save()
            return Response(Util.get_created_message(self, message=RCS))
        except Exception as e:
            print(str(e))
            service_logger.error(str(e))
            return Response(Util.get_exception_message(self, exception=e))

    def update_asset_request(self, params):
        try:
            print("Hello World")

        except Exception as e:
            print(str(e))

    def delete_asset_request(self, params):
        try:
            RequestId = params.data['RequestId']
            queryset = AssetRequestModel.objects.filter(request_id=RequestId).update(
                deleted_on=timezone.now(),
                is_deleted=1,
            )
            return Response(Util.get_deleted_message(self, message=RDS, data=queryset))
        except Exception as e:
            print(str(e))
            service_logger.error(str(e))
            return Response(Util.get_exception_message(self, exception=e))

    def get_all_assets(self, params):
        try:
            print("Hello World")

        except Exception as e:
            print(str(e))

    def get_asset_by_request_id(self, params):
        try:
            print("Hello World")

        except Exception as e:
            print(str(e))

    def filter_api(self, params):
        try:
            print("Hello World")

        except Exception as e:
            print(str(e))

    def renew_asset_request(self, params):
        try:
            print("Hello World")

        except Exception as e:
            print(str(e))

    def return_asset(self, params):
        try:
            print("Hello World")

        except Exception as e:
            print(str(e))

    def search_api(self, params):
        try:
            search_string = params.data['SearchString']
            queryset = AssetRequestModel.objects.filter(
                Q(asset_request_title__icontains=search_string) |
                Q(asset_type_lable__icontains=search_string),
                is_deleted=False
            )
            serializer = AssetRequestSerializer(queryset, many=True).data
            return Response(Util.get_fetch_message(self, message=RFS, data=serializer))

        except Exception as e:
            print(str(e))
            service_logger.error(str(e))
            return Response(Util.get_exception_message(self, exception=e))

    # ==================== SERVICE METHODS END ==================

    # ==================== Validation/Internal START ============

    # ==================== Validation/Internal END ==============
