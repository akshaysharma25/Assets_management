from django.db import models

from assets.models.base import BaseModel

DELIVERY_TYPE = (
    ("1", "Self Pick Up"),
    ("2", "Delivery Address"),
)


class AssetRequestModel(BaseModel):
    asset_request_id = models.CharField(max_length=45, null=True, blank=False)
    asset_request_title = models.CharField(blank=False, null=True)
    asset_type = models.CharField(max_length=45, null=True, blank=False)
    asset_type_name = models.CharField(max_length=45, null=True, blank=False)
    required_date = models.DateField(null=True, blank=False)
    expected_return_date = models.DateField(null=True, blank=False)
    quantity = models.IntegerField(blank=False, null=True)
    additional_notes = models.CharField(max_length=255, blank=False)
    delivery_type = models.CharField(choices=DELIVERY_TYPE, max_length=45)
    approver_name = models.CharField(max_length=255, blank=False)
    issued_on = models.DateTimeField(default='00:00:00.000000', null=True, blank=False)
    reason_for_renewal = models.CharField(max_length=255,null=True,blank=False)
