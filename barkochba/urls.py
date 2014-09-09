from django.conf.urls import patterns, url

from barkochba import views

urlpatterns = patterns('',
	url(r'^$', views.main, name='main'),
	url(r'^person/search/$', views.person_search, name='person_search'),
)