from django.conf.urls import patterns, include, url
from komodo.views import Main, Search

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^(?P<slug>[-\w]+/)$', Main),
	url(r'^(?P<slug>[-\w]+)/results/$', Search), 


    url(r'^admin/', include(admin.site.urls)),
)
