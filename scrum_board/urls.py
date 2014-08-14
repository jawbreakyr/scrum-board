from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from task import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scrum_board.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', HomeView.as_view()),
    url(r'^$', views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
