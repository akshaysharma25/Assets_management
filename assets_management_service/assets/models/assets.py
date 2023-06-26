from django.db import models
from assets.models.base import BaseModel

DELIVERY_TYPE = (
    ("SELF_PICKUP", "Self_Pick_Up"),
    ("DELIVERY_ADDRESS", "Delivery_Address"),
)

ASSET_REQUEST_STATUS = (
    ("COMPLETED", "Completed"),
    ("IN_PROGRESS", "In_Progress"),
    ("RETURNED_INITIATED", "Return_Initiated"),
    ("WAITING_FOR_APPROVAL", "Waiting_For_Approval"),
    ("WAITING_FOR_RENEWAL_APPROVAL", "Waiting_For_Renewal_Approval"),
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
    delivery_type = models.CharField(default='', choices=DELIVERY_TYPE, max_length=45)
    approver_name = models.CharField(max_length=255, blank=False)
    issued_on = models.DateTimeField(null=True, blank=True)
    reason_for_renewal = models.CharField(max_length=255, null=True, blank=False)
    asset_request_status = models.CharField(default='In_Progress', choices=ASSET_REQUEST_STATUS, max_length=45)

