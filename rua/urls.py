from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('api.urls')),
    url(r'^permissions/', include('permissions.urls')),
    url(r'^setup/', include('project_setup.urls')),
    url(r'^tools/', include('project_tools.urls')),
    url(r'^settings/', include('smart_settings.urls')),
    url(r'^user_management/', include('user_management.urls')),
    url(r'^agencies/', include('agencies.urls')),
    url(r'^acls/', include('acls.urls')),
    url(r'^common/', include('common.urls')),
    url(r'^', include('main.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
