from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include(admin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),

    (r'^api/', include('api.urls')),
)
