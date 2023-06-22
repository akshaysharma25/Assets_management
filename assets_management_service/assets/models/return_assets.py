from django.db import models
from assets.models.assets import AssetRequestModel
from assets.models.base import BaseModel


class ReturnAssetsModel(BaseModel):
    return_date = models.DateField(null=False, blank=False)
    assets_condition = models.CharField(max_length=255, null=True, blank=False)
    return_notes = models.CharField(max_length=255, null=True, blank=False)
    acknowledge_flag = models.BooleanField(max_length=45, null=True, blank=False)
    asset_request = models.ForeignKey(AssetRequestModel, blank=False, on_delete=models.CASCADE,
                                      related_name="asset_request")
