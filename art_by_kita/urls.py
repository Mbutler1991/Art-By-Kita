from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from art_by_kita.sitemaps import sitemaps
from django.views.generic import TemplateView

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('basket/', include('basket.urls')),
    path('contact/', include('contact.urls')),
    path('gallery/', include('gallery.urls')),
    path('user_messages/', include('user_messages.urls')),
    path('orders/', include('orders.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),  
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name='robots'),
]