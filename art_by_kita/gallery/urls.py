from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.PaintingListView.as_view(), name='painting_list'),
    path('<int:pk>/', views.PaintingDetailView.as_view(), name='painting_detail')
]