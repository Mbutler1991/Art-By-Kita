from django.contrib.sitemaps import Sitemap
from .models import Painting

class PaintingSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Painting.objects.all()

    def lastmod(self, obj):
        return obj.updated_at 