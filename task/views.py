from django.views import generic
from django.views.generic.edit import DeleteView
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.shortcuts import render, redirect, render_to_response
from django.contrib import auth
from django.views.generic.edit import FormMixin
from django.core.urlresolvers import reverse_lazy

# from django.contrib.auth import REDIRECT_FIELD_NAME, login
# from django.contrib.auth.forms import AuthenticationForm
# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import never_cache
# from django.views.decorators.csrf import csrf_protect
# from django.views.generic import View
# from django.views.generic.edit import FormView
# from django.conf import settings
# import urlparse

from task.forms import TaskForm
from task.models import Task


# Implementing the use of generic class based views
class TaskListView(FormMixin, generic.ListView):
    template_name = 'task/index.html'
    # context_object_name = "tasks"
    queryset = Task.objects.all()
    form_class = TaskForm
    success_url = reverse_lazy("index")


    def get_context_data(self, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        # appended the objects to the context dictionary (force)
        context['form'] = TaskForm()
        """
        pass tasks in the ff form
        {
            'story': [task1, task4, task6],
            'to do': [task2, task3, task5],
        }
        """
        task_data = None
        if self.request.user.is_authenticated:
            task_data = []
            # iterate all status choices
            # for each choice, retrieve status_id and status_name
            # then append the choice to task_data to preserve order
            for choice in Task.STATUS_CHOICES:
                task_data.append(
                    #  choice[0] status_id, choice[1] status_name
                    (choice[1], Task.objects.filter(status=choice[0])[:3]))
        context['task_data'] = task_data
        context['user'] = User
        return context

    def form_valid(self, form):
        form.save(self.request.user)
        super(TaskListView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        context = {"form": form}
        if not form.is_valid():
            return redirect('index')
        else:
            form.is_valid()
            form.save()
            return redirect('index')


def authen_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return redirect('index')
    else:
        return render(request, 'task/index.html', {
            'error_message': "Invalid Log in Details!! Please Try Again.",
        })


# class TaskDelete(DeleteView):
#     model = Task
#     success_url = reverse_lazy("index")
#     template_name = 'index.html'

# CF CF CF CF CF CF CF CF 

class TaskDelete(DeleteView):
    model = Task

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        context = {"form": form}
        if not form.is_valid():
            return redirect('index')
        else:
            form.is_valid()
            form.delete()
            return redirect('index')



# def delete(request, id):
#     note = get_object_or_404(Note, pk=id).delete()
#     return HttpResponseRedirect(reverse('notes.views.notes'))


# class TaskView(generic.TemplateView):
#     template_name = 'task.html'


"""
still cant grasp the power need more time
to carve in for mean time settle down for
function based views.
"""
# class LoginView(FormView):
#     form_class = AuthenticationForm
#     redirect_field_name = REDIRECT_FIELD_NAME
#     template_name = 'task/login.html'

#     @method_decorator(csrf_protect)
#     @method_decorator(never_cache)
#     def dispatch(self, *args, **kwargs):
#         return super(LoginView, self).dispatch(*args, **kwargs)

#     def form_valid(self, form):
#         """
#         The user has provided valid credentials (this was checked in AuthenticationForm.is_valid()). So now we
#         can check the test cookie stuff and log him in.
#         """
#         self.check_and_delete_test_cookie()
#         login(self.request, form.get_user())
#         return super(LoginView, self).form_valid(form)

#     def form_invalid(self, form):
#         """
#         The user has provided invalid credentials (this was checked in AuthenticationForm.is_valid()). So now we
#         set the test cookie again and re-render the form with errors.
#         """
#         self.set_test_cookie()
#         return super(LoginView, self).form_invalid(form)

#     def set_test_cookie(self):
#         self.request.session.set_test_cookie()


#     def get(self, request, *args, **kwargs):
#         """
#         Same as django.views.generic.edit.ProcessFormView.get(), but adds test cookie stuff
#         """
#         self.set_test_cookie()
#         return super(LoginView, self).get(request, *args, **kwargs)
