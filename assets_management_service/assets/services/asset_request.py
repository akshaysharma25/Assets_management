from rest_framework.viewsets import ViewSet
from rest_framework.viewsets import ModelViewSet
from assets.permissions.permission import PermissionChecker
from assets.utils.response.constants import *
from assets.utils.response.base_response import *
from django.db.models import Q
from django_filters.utils import timezone
from assets.utils.logger import service_logger
from assets.models.assets import AssetRequestModel
from assets.models.return_assets import ReturnAssetsModel
from assets.utils.response.util import Util
import random
from assets.serializers.asset_request_serializer import AssetRequestSerializer
from assets.models.asset_type import AssetTypeModel, AssetNameModel
from assets.serializers.asset_type_serializer import AssetTypeSerializer


class AssetServices(ViewSet, ModelViewSet):
    permission_classes = [PermissionChecker]

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
            request_id = params.query_params.get['request_id']
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
            request_id_params = params.query_params.get('request_id')
            queryset = AssetRequestModel.objects.filter(asset_request_id=request_id_params, is_deleted=False)
            serializer = AssetRequestSerializer(queryset, many=True).data
            return Response(Util.get_fetch_message(self, message=RFS, data=serializer))
        except Exception as e:
            print(str(e))
            service_logger.error(str(e))
            return Response(Util.get_exception_message(self, exception=e))

    def filter_api(self, params):
        try:
            pass

        except Exception as e:
            print(str(e))
            pass

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

    def assets_dropdown(self, params):
        try:
            queryset = AssetTypeModel.objects.all()
            serializer = AssetTypeSerializer(queryset, many=True).data
            return Response(Util.get_fetch_message(self, message=RFS, data=serializer))
        except Exception as e:
            print(str(e))
            service_logger.error(str(e))
            return Response(Util.get_exception_message(self, exception=e))

    def create_asset_type(self, params):
        try:
            asset_type_params = params.data['asset_type']
            queryset = AssetTypeModel.objects.create(asset_type=asset_type_params)
            queryset.save()
            return Response(Util.get_created_message(self, message=ASS))
        except Exception as e:
            print(str(e))
            service_logger.error(str(e))
            return Response(Util.get_exception_message(self, exception=e))

    def create_asset_name(self, params):
        try:
            asset_type_id_params = params.data['asset_type_id']
            asset_name_params = params.data['asset_name']
            description_params = params.data['description']
            queryset = AssetNameModel.objects.create(
                asset_type_id=asset_type_id_params,
                asset_name=asset_name_params,
                description=description_params
            )
            queryset.save()
            return Response(Util.get_created_message(self, message=ASS))
        except Exception as e:
            print(str(e))
            service_logger.error(str(e))
            return Response(Util.get_exception_message(self, exception=e))

    def renew_asset_request(self, params):
        try:
            request_id_params = params.data['asset_request_id']
            expected_return_date_params = params.data['expected_return_date']
            reason_for_renewal_params = params.data['reason_for_renewal']
            queryset = AssetRequestModel.objects.filter(asset_request_id=request_id_params, is_deleted=False).update(
                expected_return_date=expected_return_date_params,
                reason_for_renewal=reason_for_renewal_params,
                updated_on=timezone.now()
            )
            return Response(Util.get_created_message(self, message=RUS))
        except Exception as e:
            print(str(e))
            service_logger.error(str(e))
            return Response(Util.get_exception_message(self, exception=EX))

    def return_asset(self, params):
        try:
            return_date_params = params.data['return_date']
            assets_condition_params = params.data['assets_condition']
            return_notes_params = params.data['return_notes']
            acknowledge_flag_params = params.data['acknowledge_flag']
            asset_request_params = params.data['asset_request']
            queryset = ReturnAssetsModel.objects.create(
                return_date=return_date_params,
                assets_condition=assets_condition_params,
                return_notes=return_notes_params,
                acknowledge_flag=acknowledge_flag_params,
                asset_request_id=asset_request_params
            )
            queryset.save()
            return Response(Util.get_created_message(self, message=RCS))
        except Exception as e:
            print(str(e))
            return Response(Util.get_exception_message(self, exception=e))

    # ==================== SERVICE METHODS END ==================

    # ==================== Validation/Internal START ============

    # ==================== Validation/Internal END ==============
