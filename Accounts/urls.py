"""
URL configuration for Project App

"""

from django.urls import path
from .views import *
app_name = "user"

urlpatterns = [
    path('projects/', allprojects, name="projects"),
]