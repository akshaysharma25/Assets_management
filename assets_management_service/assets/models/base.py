from django.db import models
from .domain_model import Status


class BaseModel(models.Model):
    # Fields
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(null=True)
    deleted_on = models.DateTimeField(auto_now=False, null=True)
    is_deleted = models.BooleanField(default=False)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True,
                               blank=True, default=0)

    def soft_delete(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

    # Meta
    class Meta:
        abstract = True
