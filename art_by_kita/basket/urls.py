from django.urls import path
from . import views

app_name = 'basket'

urlpatterns = [
    path('', views.view_basket, name='view_basket'),
    path('add/<int:painting_id>/', views.add_to_basket, name='add_to_basket'),
    path('remove/<int:item_id>/', views.remove_from_basket, name='remove_from_basket'),
    path('update/<int:item_id>/', views.update_basket_item, name='update_basket_item'),
]
