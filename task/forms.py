from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm

from task.models import Task


class TaskForm(ModelForm):
	
	class Meta():
		model = Task
		fields = ('title', 'body', 'status', 'owner', 'moderator')
		widget = {'title': forms.TextInput(attrs={'placeholder': 'Search'})}

	# def save(self, user):
	# 	self.instance.created_by = user
	# 	return super(TaskForm, self).save()


# class AuthenForm(AuthenticationForm):

# 	class Meta():
# 		model = AuthenticationForm()
# 		fields = ('username', 'password')

