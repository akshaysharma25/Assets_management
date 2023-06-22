from rest_framework.viewsets import ViewSet
from rest_framework.viewsets import ModelViewSet
from assets.utils.response.constants import *
from assets.utils.response.base_response import *
from django.db.models import Q
from django_filters.utils import timezone
from assets.utils.logger import service_logger
from assets.models.assets import AssetRequestModel
from assets.utils.response.util import Util
import random
from assets.serializers.asset_request_serializer import AssetRequestSerializer
from assets.models.asset_type import AssetTypeModel, AssetNameModel
from assets.serializers.asset_type_serializer import AssetTypeSerializer


class AssetServices(ViewSet, ModelViewSet):

    # ==================== CONSTRUCTOR STARTS ===================
    def __init__(self, *args, **kwargs):
        print("Asset Service Initialized")

    # ==================== CONSTRUCTOR ENDS =====================

    # ==================== SERVICE METHODS START ================

    def create_asset_request(self, params):
        try:
            # Generate custom asset_request_id
            asset_request_id = "RQ_" + str(random.randint(111, 995))

            queryset = AssetRequestModel.objects.create(
                asset_request_id=asset_request_id,
                asset_request_title=params.data['asset_request_title'],
                asset_type=params.data['asset_type'],
                asset_type_name=params.data['asset_type_name'],
                required_date=params.data['required_date'],
                expected_return_date=params.data['expected_return_date'],
                quantity=params.data['quantity'],
                additional_notes=params.data['additional_notes'],
                delivery_type=params.data['delivery_type'],
                issued_on=params.data['issued_on'],
            )
            queryset.save()
            return Response(Util.get_created_message_withData(self, message=RCS, data={
                'asset_request_id': asset_request_id}))
        except Exception as e:
            print(str(e))
            service_logger.error(str(e))
            return Response(Util.get_exception_message(self, exception=e))

    def update_asset_request(self, params):
        try:
            data = params.data['asset_request_id']
            queryset = AssetRequestModel.objects.filter(asset_request_id=data, is_deleted=False).update(
                asset_request_title=params.data['asset_request_title'],
                asset_type=params.data['asset_type'],
                asset_type_name=params.data['asset_type_name'],
                required_date=params.data['required_date'],
                expected_return_date=params.data['expected_return_date'],
                quantity=params.data['quantity'],
                additional_notes=params.data['additional_notes'],
                delivery_type=params.data['delivery_type'],
                issued_on=params.data['issued_on'],
                updated_on=timezone.now()
            )
            return Response(Util.get_created_message(self, message=RUS))
        except Exception as e:
            print(str(e))
            service_logger.error(str(e))
            return Response(Util.get_exception_message(self, exception=EX))

    def delete_asset_request(self, params):
        try:
            request_id = params.data['request_id']
            queryset = AssetRequestModel.objects.filter(asset_request_id=request_id).update(
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
            queryset = AssetRequestModel.objects.all().filter(is_deleted=False)
            serializer = AssetRequestSerializer(queryset, many=True).data
            return Response(Util.get_fetch_message(self, message=RFS, data=serializer))
        except Exception as e:
            print(str(e))
            service_logger.error(str(e))
            return Response(Util.get_exception_message(self, exception=e))

    def get_asset_by_request_id(self, params):
        try:
            request_id = params.data['request_id']
            queryset = AssetRequestModel.objects.filter(asset_request_id=request_id, is_deleted=False)
            serializer = AssetRequestSerializer(queryset, many=True).data
            return Response(Util.get_fetch_message(self, message=RFS, data=serializer))
        except Exception as e:
            print(str(e))
            service_logger.error(str(e))
            return Response(Util.get_exception_message(self, exception=e))

    def filter_api(self, params):
        try:
            print("Hello World")

        except Exception as e:
            print(str(e))

    def search_api(self, params):
        try:
            search_string = params.data['SearchString']
            queryset = AssetRequestModel.objects.filter(
                Q(asset_request_title__icontains=search_string) |
                Q(asset_type__icontains=search_string) |
                Q(asset_type_name__icontains=search_string), is_deleted=False)
            serializer = AssetRequestSerializer(queryset, many=True).data
            return Response(Util.get_fetch_message(self, message=RFS, data=serializer))
        except Exception as e:
            print(str(e))
            service_logger.error(str(e))
            return Response(Util.get_exception_message(self, exception=e))

    # def create_asset_type(self, params):
    #     try:
    #         asset_type_params = params.data['asset_type']
    #         asset_name_params = params.data['asset_name']
    #         description_params = params.data['description']
    #
    #         asset_type = AssetTypeModel.objects.create(asset_type=asset_type_params)
    #         asset_type.save()
    #         assets_name = AssetNameModel.objects.create(asset_type_id=4,
    #                                                     asset_name=asset_name_params,
    #                                                     description=description_params)
    #         assets_name.save()
    #         return Response(Util.get_created_message(self, message=RCS))
    #     except Exception as e:
    #         print(str(e))
    #         service_logger.error(str(e))
    #         return Response(Util.get_exception_message(self, exception=e))

    def assets_dropdown(self, params):
        try:
            queryset = AssetTypeModel.objects.all()
            serializer = AssetTypeSerializer(queryset, many=True).data
            return Response(Util.get_fetch_message(self, message=RFS, data=serializer))
        except Exception as e:
            print(str(e))
            service_logger.error(str(e))
            return Response(Util.get_exception_message(self, exception=e))

    def renew_asset_request(self, params):
        try:
            print("Hello World")  # work In progress

        except Exception as e:
            print(str(e))

    def return_asset(self, params):
        try:
            print("Hello World")  # Work in Progress

        except Exception as e:
            print(str(e))

    # ==================== SERVICE METHODS END ==================

    # ==================== Validation/Internal START ============

    # ==================== Validation/Internal END ==============
