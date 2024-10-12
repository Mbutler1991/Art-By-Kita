from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class OrdersSitemap(Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return ['orders:create_order']  

    def location(self, item):
        return reverse(item)