from django.conf.urls import patterns, url

from home import views

urlpatterns = patterns('',
	url(r'^$', views.home_redirect, name='home_redirect'),
)