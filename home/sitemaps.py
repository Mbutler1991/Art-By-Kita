from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class HomeSitemap(Sitemap):
    changefreq = 'daily'  
    priority = 1.0         

    def items(self):
        return ['home:home']  

    def location(self, item):
        return reverse(item)