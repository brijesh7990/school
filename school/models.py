from django.db import models

from base.models import BaseModel


# Create your models here.


class School(BaseModel):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
