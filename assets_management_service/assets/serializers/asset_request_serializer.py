from rest_framework import serializers
from assets.models.assets import AssetRequestModel


class AssetRequestSerializer(serializers.ModelSerializer):
    asset_request_id = serializers.SerializerMethodField()

    def get_asset_request_id(self, obj):
        return obj.asset_request_id

    class Meta:
        model = AssetRequestModel
        fields = "__all__"
