from django.db import models
from django.urls import reverse
from cloudinary.models import CloudinaryField

class Painting(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    dimensions = models.CharField(max_length=50)
    materials = models.CharField(max_length=150)
    image = CloudinaryField('image', folder='paintings')
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('gallery:painting_detail', args=[str(self.id)])
