from django.conf.urls.defaults import patterns, url
from django.utils.translation import ugettext_lazy as _

from common.views import MayanCreateView, MayanDeleteView, MayanListView, MayanUpdateView

from .models import Role
from .permissions import PERMISSION_ROLE_CREATE, PERMISSION_ROLE_EDIT, PERMISSION_ROLE_VIEW


urlpatterns = patterns('permissions.views',
    url(r'^role/list/$', MayanListView.as_view(queryset=Role.objects.all(), title=_('roles'), global_permissions=[PERMISSION_ROLE_VIEW]), name='role_list'),
    url(r'^role/create/$', MayanCreateView.as_view(model=Role, global_permissions=[PERMISSION_ROLE_CREATE]), name='role_create'),
    url(r'^role/(?P<role_id>\d+)/permissions/$', 'role_permissions', (), name='role_permissions'),
    url(r'^role/(?P<role_id>\d+)/edit/$', 'role_edit', (), name='role_edit'),
    url(r'^role/(?P<role_id>\d+)/delete/$', 'role_delete', (), name='role_delete'),
    url(r'^role/(?P<role_id>\d+)/members/$', 'role_members', (), name='role_members'),

    url(r'^permissions/multiple/grant/$', 'permission_grant', (), name='permission_multiple_grant'),
    url(r'^permissions/multiple/revoke/$', 'permission_revoke', (), name='permission_multiple_revoke'),
)
