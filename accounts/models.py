from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    shipping_address = models.TextField(blank=True, null=True)
    country_code = models.CharField(max_length=5, blank=True, null=True)
    phone_number = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.username