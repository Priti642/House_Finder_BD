from django.urls import path
from django.contrib.auth import views as auth_views
from user.views import *

urlpatterns = [
    # Login Page
    path('login/', login_view, name='Login'),
    # Register Page
    path('register/', register_view, name='Register'),
    # Logout Page
    path('logout/', logout_view, name='Logout'),

    # Password Reset Pages
    path('password_reset/', password_reset_view, name='Password Reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password/password_reset_complete.html'), name='password_reset_complete'),
]
