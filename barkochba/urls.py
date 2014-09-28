from django.conf.urls import patterns, url

from barkochba import views

urlpatterns = patterns('',
	url(r'^$', views.main, name='main'),
	url(r'^edit/(?P<story_id>\d+)/$', views.story_edit, name='edit'),
)