from django.contrib.sitemaps import Sitemap
from .models import Painting

class PaintingSitemap(Sitemap):
    changefreq = 'weekly'  
    priority = 0.5          

    def items(self):
        return Painting.objects.all()  

    def location(self, item):
        return item.get_absolute_url()