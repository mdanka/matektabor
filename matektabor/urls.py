from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'matektabor.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	url(r'^barkochba/', include('barkochba.urls', namespace="barkochba")),
	url(r'^admin/', include(admin.site.urls)),
)
