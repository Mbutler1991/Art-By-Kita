from django.urls import path
from . import views

app_name = 'user_messages'


urlpatterns = [
    path('staff-inbox/', views.staff_inbox, name='staff_inbox'),
    path('message/<int:pk>/', views.message_detail, name='message_detail'),
]
