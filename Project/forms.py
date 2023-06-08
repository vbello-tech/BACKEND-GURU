from django import forms
from .models import *

class CreateProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('project_name', 'project_description', 'project_image', 'project_url', 'github_url', )

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('review',)

        widgets = {
            'comment': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    "placeholder": 'Enter your comment here',
                    'rows': 5,
                    'cols': 30,
                }
            )

        }