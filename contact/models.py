from django.db import models
from django.conf import settings 


class Contact(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)  
    reply = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Message from {self.name} on {self.created_at.strftime('%m/%d/%Y')}"
