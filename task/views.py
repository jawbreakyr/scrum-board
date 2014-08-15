from django.shortcuts import render, render_to_response
from django.views import generic

from task.forms import TaskForm
from task.models import Task


# def home(request):
#   tasks = Task.objects.all()
#   form = TaskForm()
#   c = {'form': form, 'tasks': tasks }
#   return render(request, 'task/home.html', c)


# Implementing the use of generic class based views
class PublisherView(generic.ListView):
    template_name = 'task/home.html'
    # context_object_name = "tasks"
    queryset = Task.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PublisherView, self).get_context_data(**kwargs)
        # appended the objects to the context dictionary (force)
        context['form'] = TaskForm()
        # appended the objects to the context dictionary (force)
        context['tasks'] = Task.objects.all()
        return context
