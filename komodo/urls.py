from django.conf.urls import patterns, include, url
from komodo.views import Main, Search
from django.views.generic import RedirectView
from django.conf.urls import handler404, handler500
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', RedirectView.as_view(url='/g/')),
	url(r'^(?P<slug>[-\w]+/)$', Main),
	url(r'^(?P<slug>[-\w]+/)results/$', Search), 


    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

