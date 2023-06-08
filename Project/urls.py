"""
URL configuration for Project App

"""

from django.urls import path
from .views import *
app_name = "project"

urlpatterns = [
    path('create-project/', CreateProjectView.as_view(), name="create_project"),
    path('all-projects/', ProjectListView.as_view(), name="project_list"),
    path('project/<str:name>/<str:slug>/', ProjectDetailView.as_view(), name="project_detail"),
    path('delete-project/<str:slug>/', delete, name="delete"),
]