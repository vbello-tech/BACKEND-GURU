"""
URL configuration for Challenge App

"""

from django.urls import path
from .views import *
app_name = "challenege"

urlpatterns = [
    path('', welcome, name="welcome"),
]