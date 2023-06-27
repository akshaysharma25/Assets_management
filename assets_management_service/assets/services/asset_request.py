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
    # permission_classes = [PermissionChecker]

    # ==================== CONSTRUCTOR STARTS ===================
    def __init__(self, *args, **kwargs):
        print("Asset Service Initialized")

    # ==================== CONSTRUCTOR ENDS =====================

    # ==================== SERVICE METHODS START ================

    def create_asset_request(self, params):
        try:
            # Generate custom asset_request_id
            asset_request_id = "RQ_" + str(random.randint(1000, 5000))

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
                delivery_address=params.data['delivery_address'],
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
                delivery_address=params.data['delivery_address'],
                updated_on=timezone.now()
            )
            return Response(Util.get_created_message(self, message=RUS))
        except Exception as e:
            print(str(e))
            service_logger.error(str(e))
            return Response(Util.get_exception_message(self, exception=EX))

    def delete_asset_request(self, params):
        try:
            asset_request_id = params.query_params.get('asset_request_id')
            queryset = AssetRequestModel.objects.filter(asset_request_id=asset_request_id).update(
                deleted_on=timezone.now(),
                is_deleted=True)
            return Response(Util.get_deleted_message(self, message=RDS))
        except Exception as e:
            print(str(e))
            service_logger.error(str(e))
            return Response(Util.get_exception_message(self, exception=e))

    def get_all_assets(self, params):
        try:
            queryset = AssetRequestModel.objects.all().filter(is_deleted=False).order_by('-created_on', '-updated_on')
            serializer = AssetRequestSerializer(queryset, many=True).data
            return Response(Util.get_fetch_message(self, message=RFS, data=serializer))
        except Exception as e:
            print(str(e))
            service_logger.error(str(e))
            return Response(Util.get_exception_message(self, exception=e))

    def get_asset_by_request_id(self, params):
        try:
            asset_request_id = params.query_params.get('asset_request_id')
            queryset = AssetRequestModel.objects.filter(asset_request_id=asset_request_id, is_deleted=False)
            if queryset:
                serializer = AssetRequestSerializer(queryset, many=True).data
                return Response(Util.get_fetch_message(self, message=RFS, data=serializer))
            return Response(Util.get_no_record_message(self, message=RNF))
        except Exception as e:
            print(str(e))
            service_logger.error(str(e))
            return Response(Util.get_exception_message(self, exception=e))

    def filter_api(self, request):
        try:

            # Params
            asset_type = request.query_params.get('asset_type')
            asset_name = request.query_params.get('asset_name')
            request_date = request.query_params.get('request_date')
            issued_date = request.query_params.get('issued_date')
            due_date = request.query_params.get('due_date')

            queryset = AssetRequestModel.objects.filter(is_deleted=False)
            if asset_type:
                queryset = queryset.filter(Q(asset_type__icontains=asset_type))
            if asset_name:
                queryset = queryset.filter(Q(asset_type_name__icontains=asset_name))
            if request_date:
                queryset = queryset.filter(Q(request_date=request_date))
            if issued_date:
                queryset = queryset.filter(Q(created_on=issued_date))
            if due_date:
                queryset = queryset.filter(Q(expected_return_date=due_date))
            serializer = AssetRequestSerializer(queryset, many=True).data
            return Response(Util.get_fetch_message(self, message=RFS, data=serializer))
        except Exception as e:
            print(str(e))
            return Response(Util.get_exception_message(self, exception=e))

    def search_api(self, params):
        try:
            search_string = params.query_params.get('SearchString')
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
            queryset = AssetNameModel.objects.create(
                asset_type_id=params.data['asset_type_id'],
                asset_name=params.data['asset_name'],
                description=params.data['description'])
            queryset.save()
            return Response(Util.get_created_message(self, message=ASS))
        except Exception as e:
            print(str(e))
            service_logger.error(str(e))
            return Response(Util.get_exception_message(self, exception=e))

    def renew_asset_request(self, params):
        try:
            # Check Whether that assert is present in table:
            asset_request = AssetRequestModel.objects.filter(asset_request_id=params.data['asset_request_id'], is_deleted=False)
            if asset_request:
                queryset = AssetRequestModel.objects.filter(
                    asset_request_id=params.data['asset_request_id'], is_deleted=False).update(
                    expected_return_date=params.data['expected_return_date'],
                    reason_for_renewal=params.data['reason_for_renewal'],
                    asset_request_status=params.data['asset_request_status'],
                    updated_on=timezone.now())
                return Response(Util.get_created_message(self, message=RUS))
            return Response(Util.get_no_record_message(self, message=RNF))
        except Exception as e:
            print(str(e))
            service_logger.error(str(e))
            return Response(Util.get_exception_message(self, exception=EX))

    def return_asset(self, params):
        try:
            # Check Whether that assert is present in table:
            asset_request = AssetRequestModel.objects.filter(id=params.data['asset_request_id'], is_deleted=False)
            if asset_request:
                return_asset = ReturnAssetsModel.objects.create(
                    asset_request_id=params.data['asset_request_id'],
                    return_date=params.data['return_date'],
                    assets_condition=params.data['assets_condition'],
                    return_notes=params.data['return_notes'],
                    acknowledge_flag=params.data['acknowledge_flag'])
                return_asset.save()
                # Updating the status of asset in asset_request table i.e asset_request_status=Return_Initiated
                asset_request_update = AssetRequestModel.objects.filter(
                    id=params.data['asset_request_id']).update(
                    asset_request_status=params.data['asset_request_status'])
                return Response(Util.get_created_message(self, message=RCS))
            return Response(Util.get_no_record_message(self, message=RNF))
        except Exception as e:
            print(str(e))
            return Response(Util.get_exception_message(self, exception=e))

    def update_asset_request_status(self, params):
        try:
            print("1")
            query_sets = AssetRequestModel.objects.filter(asset_request_id=params.data['asset_request_id'],is_deleted=False)
            print("query_sets", query_sets)
            if query_sets:
                queryset = AssetRequestModel.objects.filter(
                    asset_request_id=params.data['asset_request_id'], is_deleted=False).update(
                    asset_request_status=params.data['asset_request_status'],
                    issued_on=params.data['issued_on'],

                    updated_on=timezone.now())
                return Response(Util.get_created_message(self, message=RSUS))
            return Response(Util.get_no_record_message(self, message=RNF))
        except Exception as e:
            print(str(e))
            return Response(Util.get_exception_message(self, exception=e))

    # ==================== SERVICE METHODS END ==================

    # ==================== Validation/Internal START ============

    # ==================== Validation/Internal END ==============
