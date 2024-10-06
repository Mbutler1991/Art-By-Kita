from django.urls import path
from . import views

app_name = 'user_messages'


urlpatterns = [
    path('inbox/', views.customer_inbox, name='inbox'),
    path('staff-inbox/', views.staff_inbox, name='staff_inbox'),
    path('reply/<int:message_id>/', views.reply_to_message, name='reply_to_message'),
    path('message/<int:pk>/', views.message_detail, name='message_detail'),
    path('message/<int:pk>/reply/', views.message_reply, name='message_reply'),
]
