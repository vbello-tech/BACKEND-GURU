"""
URL configuration for Project App

"""

from django.urls import path
from .views import *
app_name = "project"

urlpatterns = [
    path('create-project/', CreateProjectView.as_view(), name="create_project"),
    path('all-projects/', ProjectListView.as_view(), name="project_list"),
    path('project/<str:name>/<int:pk>/', projectdetail, name="project_detail"),
]