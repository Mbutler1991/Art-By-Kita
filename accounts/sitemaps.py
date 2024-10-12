from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class AccountsSitemap(Sitemap):
    priority = 0.6
    changefreq = 'weekly'

    def items(self):
        return [
            'accounts:login',
            'accounts:logout',
            'accounts:register',
        ]

    def location(self, item):
        return reverse(item)