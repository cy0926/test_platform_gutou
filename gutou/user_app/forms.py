from django import forms
from user_app.models.project import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'describe', 'status']
