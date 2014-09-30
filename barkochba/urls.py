from django.conf.urls import patterns, url

from barkochba import views

urlpatterns = patterns('',
	url(r'^$', views.main, name='main'),
	url(r'^update-people/$', views.story_update_people, name='update_people'),
)