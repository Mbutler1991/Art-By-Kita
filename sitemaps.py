from django.contrib.sitemaps import Sitemap
from django.contrib.sitemaps.views import sitemap
from django.urls import path
from home.sitemaps import HomeSitemap
from gallery.sitemaps import PaintingSitemap
from accounts.sitemaps import AccountsSitemap
from contact.sitemaps import ContactSitemap
from orders.sitemaps import OrdersSitemap
from basket.sitemaps import BasketSitemap

sitemaps = {
    'home': HomeSitemap,
    'paintings': PaintingSitemap,
    'accounts': AccountsSitemap,
    'contact': ContactSitemap,
    'orders': OrdersSitemap,
    'basket': BasketSitemap,
}
