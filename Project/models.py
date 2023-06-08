from django.db import models
from django.utils import timezone
from django.conf import settings
from Accounts.models import User as user
from django.shortcuts import reverse
import random, string

# Create your models here.

def slug_code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))

class Project(models.Model):
    author = models.ForeignKey(user, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=250)
    project_description = models.TextField()
    project_image = models.ImageField(upload_to="project/")
    project_url = models.URLField(blank=True, null=True)
    github_url = models.URLField()
    posted_date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(default=slug_code())

    def get_url(self):
        return reverse("project:project_detail", kwargs={
            'slug': self.slug,
            'name':self.project_name
        })

    def delete(self):
        return reverse("project:delete", kwargs={
            'slug':self.slug,
        })

    def __str__(self):
        return self.project_name

class Review(models.Model):
    post = models.ForeignKey('Project', related_name="project_reviews", on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.TextField()
    comment_date = models.DateField(default=timezone.now)


    def __str__(self):
        return f"review {self.pk} on project { self.post.project_name } by { self.post.author }"