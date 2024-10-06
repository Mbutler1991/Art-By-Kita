from django.db import models
from django.conf import settings

class UserMessage(models.Model):
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='customer_messages'
    )
    staff = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        related_name='staff_messages', 
        null=True, 
        blank=True
    )
    message = models.TextField()
    reply = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.customer.username} on {self.created_at.strftime('%Y-%m-%d')}"

