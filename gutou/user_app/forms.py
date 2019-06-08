from django import forms
from user_app.models.project import Project
from user_app.models.module import Module


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'describe', 'status']


class ModuleForm(forms.ModelForm):

    class Meta:
        model = Module
        fields = ['project', 'name', 'describe']
