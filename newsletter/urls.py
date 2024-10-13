from django.urls import path
from . import views

app_name = "newsletter"

urlpatterns = [
    path('signup/', views.newsletter_signup, name='newsletter_signup'),
    path('thank-you/', views.newsletter_thankyou, name='newsletter_thankyou'),
]