from django.conf.urls import patterns, url

from export import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	# pl: /export/3/
	url(r'^(?P<camp_id>\d+)/$', views.camp_export, name='camp_export'),
)
