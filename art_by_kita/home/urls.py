from django.urls import path, reverse
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home_view, name='home'),
]