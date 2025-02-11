# userauth/urls.py
from django.urls import path
from .views import register_view, login_view

app_name = 'userauth'  # Define app_name here

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
]
