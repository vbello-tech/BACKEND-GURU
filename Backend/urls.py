"""
URL configuration for Backend project.
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("Challenge.urls", namespace="challenge")),
    path('project/', include("Project.urls", namespace="project")),
    path('accounts/', include("Accounts.urls", namespace="user")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)