from django.db import models
from assets.models.base import BaseModel


class AssetTypeModel(BaseModel):
    asset_type = models.CharField(max_length=45, null=True, blank=False, unique=True)

    def __str__(self):
        return self.asset_type


class AssetNameModel(BaseModel):
    asset_type = models.ForeignKey(AssetTypeModel, blank=False, on_delete=models.CASCADE, related_name="asset_name")
    asset_name = models.CharField(max_length=45, blank=False, null=True)
    description = models.CharField(max_length=255, blank=False, null=True)


    def __str__(self):
        return self.asset_name


