from django.conf.urls import patterns, include, url
from komodo.views import Main, Search

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', Main),
	url(r'^search/g/$', Search), 


    url(r'^admin/', include(admin.site.urls)),
)
