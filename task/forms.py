from django.forms import ModelForm

from task.models import Task


class TaskForm(ModelForm):
	
	class Meta():
		model = Task
		fields = ('title', 'body', 'status',)

	def clean(self):
		title = self.cleaned_data.POST.get('title')
		body = self.cleaned_data.POST.get('body')
		status = self.cleaned_data.POST.get('status')

		return self.cleaned_data

