from django.urls import path
from .views import contact_view, thank_you_view

app_name = 'contact'

urlpatterns = [
    path('contact/', contact_view, name='contact'),
    path('thank-you/', thank_you_view, name='thank_you'),  
]