from django.views import generic
from django.contrib.auth import REDIRECT_FIELD_NAME, login
from django.contrib.auth.forms import AuthenticationForm
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic import View
from django.views.generic.edit import FormView
from django.conf import settings
from django.contrib.auth.models import User

import urlparse

from task.forms import TaskForm
from task.models import Task


# def home(request):
#   tasks = Task.objects.all()
#   form = TaskForm()
#   c = {'form': form, 'tasks': tasks }
#   return render(request, 'task/home.html', c)


# Implementing the use of generic class based views
class PublisherView(generic.ListView):
    template_name = 'task/index.html'
    # context_object_name = "tasks"
    queryset = Task.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PublisherView, self).get_context_data(**kwargs)
        # appended the objects to the context dictionary (force)
        context['form'] = TaskForm()
        """
        pass tasks in the ff form
        {
            'story': [task1, task4, task6],
            'to do': [task2, task3, task5],
        }
        """
        task_data = []
        for choice in Task.STATUS_CHOICES:  # ready the keys
            task_data.append(
                (choice[1], Task.objects.all().filter(status=choice[0])))
        context['task_data'] = task_data
        context['user'] = User
        return context


class LoginView(FormView):
    form_class = AuthenticationForm
    redirect_field_name = REDIRECT_FIELD_NAME
    template_name = 'task/login.html'

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super(LoginView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        """
        The user has provided valid credentials (this was checked in AuthenticationForm.is_valid()). So now we
        can check the test cookie stuff and log him in.
        """
        self.check_and_delete_test_cookie()
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)

    def form_invalid(self, form):
        """
        The user has provided invalid credentials (this was checked in AuthenticationForm.is_valid()). So now we
        set the test cookie again and re-render the form with errors.
        """
        self.set_test_cookie()
        return super(LoginView, self).form_invalid(form)

    def set_test_cookie(self):
        self.request.session.set_test_cookie()


    def get(self, request, *args, **kwargs):
        """
        Same as django.views.generic.edit.ProcessFormView.get(), but adds test cookie stuff
        """
        self.set_test_cookie()
        return super(LoginView, self).get(request, *args, **kwargs)
