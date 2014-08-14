from django.shortcuts import render
from django.views import generic

from task.forms import TaskForm
from task.models import Task


def home(request):
	tasks = Task.objects.all()
	form = TaskForm()
	c = {'form': form, 'tasks': tasks }
	return render(request, 'task/home.html', c)

# class HomeView(generic.TemplateView):
# 	template_name = 'task/home.html'

# 	def get(self, request, *args, **kwargs):
# 		context = {"form": TaskForm()}
# 		return self.render_to_response(context)