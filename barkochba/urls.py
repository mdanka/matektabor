from django.conf.urls import patterns, url

from barkochba import views

urlpatterns = patterns('',
	url(r'^$', views.main, name='main'),
)