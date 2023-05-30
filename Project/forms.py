from django import forms
from .models import *

class CreateProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('project_name', 'project_description', 'project_image', 'project_url', 'github_url', )