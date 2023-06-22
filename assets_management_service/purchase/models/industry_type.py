from django.db import models
from assets.models.base import BaseModel


class IndustryTypeModel(BaseModel):
    industry_type = models.CharField(max_length=45, null=True, blank=False)