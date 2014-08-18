from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm

from task.models import Task


class TaskForm(ModelForm):
	
	class Meta():
		model = Task
		fields = ('title', 'body', 'status',)
		widget = {'title': forms.TextInput(attrs={'placeholder': 'Search'})}

	def clean(self):
		title = self.cleaned_data.POST.get('title')
		body = self.cleaned_data.POST.get('body')
		status = self.cleaned_data.POST.get('status')

		return self.cleaned_data


# class AuthenForm(AuthenticationForm):

# 	class Meta():
# 		model = AuthenticationForm()
# 		fields = ('username', 'password')

