from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'rua.views.home', name='home'),
    # url(r'^rua/', include('rua.foo.urls')),
    url(r'^admin/', include(admin.site.urls)),

    (r'^api/', include('api.urls')),
)
