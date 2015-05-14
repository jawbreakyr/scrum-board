from django.conf.urls import patterns, include, url
from django.contrib.auth.forms import AuthenticationForm

from django.contrib import admin
admin.autodiscover()

# from task.views import HomeView
# from task.models import Task
from task.views import TaskListView, TaskDelete
from task import views


urlpatterns = patterns('',
    url(r'^$', TaskListView.as_view(), name='index'),
        # queryset = Task.objects.all(),
        # context_object_name="tasks",
        # )),
    # url(r'^delete/(?P<pk>\d+)/', TaskDelete.as_view(), name="delete"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'},
        name='logout'),
    url(r'^authen/', views.authen_view, name='authen_view'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^delete/(?P<pk>\d+)/$',
        TaskDelete.as_view(), name='delete-comment'),
)
