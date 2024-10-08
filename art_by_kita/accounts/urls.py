from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html', redirect_authenticated_user=True, next_page='home:home'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home:home'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('password_change/', PasswordChangeView.as_view(template_name='accounts/password_change_form.html'), name='password_change'),
    path('password_change_done/', PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'), name='password_change_done'),
]