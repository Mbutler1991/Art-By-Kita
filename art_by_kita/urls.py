from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from art_by_kita.sitemaps import sitemaps
from django.views.generic import TemplateView
from . import views

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
    path('newsletter/', views.newsletter_signup, name='newsletter_signup'),
    path('thank-you/', views.thank_you, name='newsletter_thankyou'),
]