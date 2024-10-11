from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.PaintingListView.as_view(), name='painting_list'),
    path('<int:pk>/', views.PaintingDetailView.as_view(), name='painting_detail'),
    path('manage/', views.manage_paintings, name='manage_paintings'),
    path('manage/create/', views.create_painting, name='create_painting'),
    path('manage/edit/<int:painting_id>/', views.edit_painting, name='edit_painting'),
    path('manage/delete/<int:painting_id>/', views.delete_painting, name='delete_painting'),
]