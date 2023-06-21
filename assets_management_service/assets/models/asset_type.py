from django.db import models
from assets.models.base import BaseModel


class AssetTypeModel(BaseModel):
    asset_type = models.CharField(max_length=45, null=True, blank=False)


class AssetNameModel(BaseModel):
    asset_type = models.ForeignKey(AssetTypeModel, blank=False, on_delete=models.CASCADE, related_name="asset_name")
    asset_name = models.CharField(blank=False, null=True)
    description = models.CharField(blank=False, null=True)
