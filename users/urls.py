from django.urls import path, include
from . import views

"""Defines URL patterns for users""" 

app_name = 'users' 

urlpatterns = [
    # Include default auth urls.

    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
]
