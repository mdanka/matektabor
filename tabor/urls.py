from django.conf.urls import patterns, url

from tabor import views

urlpatterns = patterns('',
	url(r'^person/search/$', views.person_search, name='person_search'),
)