from django.conf.urls import patterns, include, url

import session_csrf
session_csrf.monkeypatch()

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djtest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^_ah/', include('djangae.urls')),
    
    
    url(r'^$','webdisplay.views.home', name='home'),
#    url(r'^set_temp/$', 'webdisplay.views.set_temp', name='set_temp'),
#    url(r'^get_nest/$', 'webdisplay.views.get_nest', name='get_nest'),
    url(r'^get_data/$', 'webdisplay.views.get_data', name='get_data'),
    url(r'^set_temp/$', 'webdisplay.views.set_temp', name='set_temp'),



    # Note that by default this is also locked down with login:admin in app.yaml
    url(r'^admin/', include(admin.site.urls)),

    url(r'^csp/', include('cspreports.urls')),

    url(r'^auth/', include('djangae.contrib.gauth.urls')),
)
