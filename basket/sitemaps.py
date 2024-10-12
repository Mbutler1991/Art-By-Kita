from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class BasketSitemap(Sitemap):
    priority = 0.6
    changefreq = 'weekly'

    def items(self):
        return ['basket:cart']

    def location(self, item):
        return reverse(item)