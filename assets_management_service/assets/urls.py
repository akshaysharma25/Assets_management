from django.urls import path

from assets.services.asset_request import AssetServices

urlpatterns = [

    # Assets APIs
    path('assets/create', AssetServices.as_view({'post': 'create_asset_request'}), name="create_asset_request"),
    path('assets/update', AssetServices.as_view({'put': 'update_asset_request'}), name="update_asset_request"),
    path('assets/delete', AssetServices.as_view({'delete': 'delete_asset_request'}), name="delete_asset_request"),
    path('assets/get_all', AssetServices.as_view({'get': 'get_all_assets'}), name="get_all_assets"),
    path('assets/get_asset_by_request_id', AssetServices.as_view({'get': 'get_asset_by_request_id'}), name="get_asset_by_request_id"),
    path('assets/filter', AssetServices.as_view({'get': 'filter_api'}), name="filter_api"),
    path('assets/search', AssetServices.as_view({'get': 'search_api'}), name="search_api"),
    path('assets/create_asset_type', AssetServices.as_view({'post': 'create_asset_type'}), name="create_asset_type"),
    path('assets/create_asset_name', AssetServices.as_view({'post': 'create_asset_name'}), name="create_asset_name"),
    path('assets/assets_dropdown', AssetServices.as_view({'get': 'assets_dropdown'}), name="assets_dropdown"),
    path('assets/renew_asset_request', AssetServices.as_view({'post': 'renew_asset_request'}), name="renew_asset_request"),
    path('assets/return_asset', AssetServices.as_view({'post': 'return_asset'}), name="return_asset"),

]
