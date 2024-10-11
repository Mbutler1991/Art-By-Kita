from django.db import models
from django.conf import settings
from accounts.models import CustomUser

class UserMessage(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    email = models.EmailField(default='N/A')
    name = models.CharField(max_length=255, default='Anonymous')
    phone = models.CharField(max_length=20, default='N/A')
    message = models.TextField() 

    def __str__(self):
        return f"Message from {self.customer.username} on {self.created_at.strftime('%Y-%m-%d')}"

