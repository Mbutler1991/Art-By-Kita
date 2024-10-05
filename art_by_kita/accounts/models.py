from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    shipping_address = models.TextField()
    phone_number = models.CharField(max_length=30)  # Longer length to allow for international numbers

    def __str__(self):
        return self.user.username