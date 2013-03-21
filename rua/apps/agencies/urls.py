from __future__ import absolute_import

from django.conf.urls import patterns, url
from django.contrib.auth.models import User, Group
from django.utils.translation import ugettext_lazy as _

from common.views import MayanCreateView, MayanDeleteView, MayanListView, MayanUpdateView

from .models import Agency
#from .permissions import PERMISSION_GROUP_VIEW, PERMISSION_USER_VIEW

urlpatterns = patterns('agencies.views',
    url(r'^list/$', MayanListView.as_view(#global_permissions=[PERMISSION_USER_VIEW],
        title=_('agencies'),
        queryset=Agency.objects.all(),
        hide_link=True,
        multi_select_as_buttons=True), name='agency_list'),
    url(r'^add/$', 'agency_add', (), 'agency_add'),
    url(r'^(?P<agency_pk>\d+)/edit/$', 'agency_edit', (), 'agency_edit'),
    url(r'^(?P<agency_pk>\d+)/delete/$', 'agency_delete', (), 'agency_delete'),
    url(r'^multiple/delete/$', 'agency_multiple_delete', (), 'agency_multiple_delete'),

    url(r'^(?P<agency_pk>\d+)/position/list/$', 'position_list', (), 'position_list'),
    url(r'^(?P<agency_pk>\d+)/position/add/$', 'position_add', (), 'position_add'),
    url(r'^position/(?P<position_pk>\d+)/edit/$', 'position_edit', (), 'position_edit'),
    url(r'^position/(?P<position_pk>\d+)/delete/$', 'position_delete', (), 'position_delete'),
)
