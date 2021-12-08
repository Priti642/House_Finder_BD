from django.urls import path
from user.views import login_view, register_view, logout_view


urlpatterns = [
    # Login Page
    path('login/', login_view, name='Login'),
    # Register Page
    path('register/', register_view, name='Register'),
    # Logout Page
    path('logout/', logout_view, name='Logout'),
]
