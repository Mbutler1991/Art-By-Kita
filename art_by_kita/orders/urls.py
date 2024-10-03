from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/<int:painting_id>/', views.create_order, name='create_order'),
    path('success/<int:order_id>/', views.order_success, name='order_success'),
    path('cancel/', views.order_cancel, name='order_cancel'),
]