from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm

from task.models import Task


class TaskForm(ModelForm):
    class Meta():
        model = Task
        fields = ('title', 'body', 'status', 'owner', 'moderator')
        widget = {'title': forms.TextInput(attrs={'placeholder': 'Search'})}
