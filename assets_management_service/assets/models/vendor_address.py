from django.db import models
from assets.models.base import BaseModel


class VendorAddressModel(BaseModel):
    locality = models.CharField(max_length=100, null=True, blank=False)
    country = models.CharField(max_length=45, null=True, blank=False)
    state = models.CharField(max_length=45, null=True, blank=False)
    city = models.CharField(max_length=45, null=True, blank=False)
    pincode = models.IntegerField(max_length=45, null=True, blank=False)