from rest_framework.viewsets import ViewSet, ModelViewSet


class AssetServices(ViewSet, ModelViewSet):

    # ==================== CONSTRUCTOR STARTS ===================
    def __init__(self, *args, **kwargs):
        print("Asset Service Initialized")

    # ==================== CONSTRUCTOR ENDS =====================

    # ==================== SERVICE METHODS START ================

    def create_asset_request(self, params):
        try:
            print("Hello World")

        except Exception as e:
            print(str(e))

    def update_asset_request(self, params):
        try:
            print("Hello World")

        except Exception as e:
            print(str(e))

    def delete_asset_request(self, params):
        try:
            print("Hello World")

        except Exception as e:
            print(str(e))

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



    # ==================== SERVICE METHODS END ==================

    # ==================== Validation/Internal START ============

    # ==================== Validation/Internal END ==============
