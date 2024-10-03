from django.contrib import admin
from .models import Painting

class PaintingAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'dimension', 'materials', 'description', 'price')
    search_fields = ('name', 'description', 'materials')
