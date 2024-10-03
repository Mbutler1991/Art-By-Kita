from django.db import models
from django.contrib.auth.models import User
from gallery.models import Painting

class Basket(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='basket')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Basket of {self.user.username}"

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='items')
    painting = models.ForeignKey(Painting, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.painting.name}"

    def get_cost(self):
        return self.quantity * self.painting.price
