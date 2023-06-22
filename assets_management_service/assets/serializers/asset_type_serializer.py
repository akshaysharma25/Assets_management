from rest_framework import serializers
from assets.models.asset_type import AssetNameModel, AssetTypeModel


class AssetNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetNameModel
        fields = ['asset_type', 'asset_name', 'description']


class AssetTypeSerializer(serializers.ModelSerializer):
    asset_name = AssetNameSerializer(many=True, read_only=True)

    class Meta:
        model = AssetTypeModel
        fields = ['id', 'asset_type', 'asset_name']


