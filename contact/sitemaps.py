from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class ContactSitemap(Sitemap):
    changefreq = 'monthly'  
    priority = 0.5

    def items(self):
        return ['contact:contact', 'contact:thank_you']  

    def location(self, item):
        return reverse(item)