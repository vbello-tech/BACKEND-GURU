from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.


class Project(models.Model):
    author = models.ForeignKey('settings.AUTH_USER_MODEL', on_delete=models.CASCADE)
    project_name = models.CharField(max_length=250)
    project_description = models.TextField()
    project_image = models.ImageField(upload_to="project/")
    project_url = models.URLField(blank=True, null=True)
    github_url = models.URLField()
    published_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.project_name
