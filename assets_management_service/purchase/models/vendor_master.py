from django.db import models
from assets.models.base import BaseModel
from assets.models.vendor_address import VendorAddressModel
from purchase.models.industry_type import IndustryTypeModel

VENDOR_TYPE = (
    ("1", "Company"),
    ("2", "Individual"),
)


class VendorModel(BaseModel):
    vendor_id = models.CharField(max_length=45, null=True, blank=False)
    company_name = models.CharField(max_length=45, null=True, blank=False)
    full_name = models.CharField(max_length=45, null=True, blank=False)
    vendor_website = models.CharField(max_length=45, null=True, blank=False)
    vendor_contact_email = models.EmailField(max_length=45, null=True, blank=False)
    vendor_contact_alt_email = models.EmailField(max_length=45, null=True, blank=False)
    vendor_contact_no = models.IntegerField(max_length=45, null=True, blank=False)
    vendor_contact_alt_no = models.IntegerField(max_length=45, null=True, blank=False)
    gst_number = models.CharField(max_length=45, null=True, blank=False)
    currency = models.CharField(max_length=45, null=True, blank=False)
    duns = models.CharField(max_length=45, null=True, blank=False)
    payment_terms = models.CharField(max_length=45, null=True, blank=False)
    contact_person_info = models.JSONField()
    industry_type = models.ForeignKey(IndustryTypeModel, blank=False, on_delete=models.CASCADE, related_name="industry_type")
    vendor_address = models.ForeignKey(VendorAddressModel, blank=False, on_delete=models.CASCADE, related_name="vendor_address")