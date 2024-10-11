from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('basket/', include('basket.urls')),
    path('contact/', include('contact.urls')),
    path('gallery/', include('gallery.urls')),
    path('user_messages/', include('user_messages.urls')),
    path('orders/', include('orders.urls')),
]
