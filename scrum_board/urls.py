from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

# from task.views import HomeView
from task.models import Task
from task.views import PublisherView

urlpatterns = patterns('',
	url(r'^$', PublisherView.as_view()),
		# queryset = Task.objects.all(),
		# context_object_name="tasks",
		# )),
    # Examples:
    # url(r'^$', 'scrum_board.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^$', HomeView.as_view()),
    # url(r'^$', views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
