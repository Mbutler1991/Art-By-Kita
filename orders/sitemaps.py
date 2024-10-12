from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class OrdersSitemap(Sitemap):
    changefreq = 'daily'  
    priority = 0.6        

    def items(self):
        return [
            'orders:create_order',
            'orders:order_success',
            'orders:order_cancel',
        ]
    
    def location(self, item):
        return reverse(item)
    