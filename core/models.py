from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4
from django.utils.translation import gettext as _

# Create your models here.
class BaseModel(models.Model):
    id = models.UUIDField(editable=False, primary_key=True, default=uuid4)

    class Meta:
        abstract = True

class MyManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

class SoftDeleteModel(BaseModel):
    
    is_deleted = models.BooleanField(default=False, db_index=True)

    def delete(self):
        self.is_deleted = True
        self.save()
    
    class Meta:
        abstract = True
    
class TimStampMixin:
    create_at = models.DateTimeField(_("create at"), auto_now=False, auto_now_add=True)
    update_at = models.DateTimeField(_("update at"), auto_now=True, auto_now_add=False)

