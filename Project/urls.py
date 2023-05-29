"""
URL configuration for Project App

"""

from django.urls import path
from .views import *
app_name = "project"

urlpatterns = [
    path('projects/', allprojects, name="projects"),
]