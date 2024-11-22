from django.contrib import admin
from .models import Painting


class PaintingAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'price', 'dimensions', 'materials', 'description', 'price'
        )
    search_fields = ('title', 'description', 'materials')


admin.site.register(Painting, PaintingAdmin)
