from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from navigation.classes import Link

from .icons import (icon_agency, icon_agency_add, icon_agency_edit, icon_agency_delete,
    icon_position, icon_position_add, icon_position_edit, icon_position_delete,
    icon_department, icon_department_add, icon_department_edit, icon_department_delete)
from .permissions import (PERMISSION_AGENCY_CREATE, PERMISSION_AGENCY_EDIT,
    PERMISSION_AGENCY_VIEW, PERMISSION_AGENCY_DELETE, PERMISSION_POSITION_CREATE, PERMISSION_POSITION_EDIT,
    PERMISSION_POSITION_VIEW, PERMISSION_POSITION_DELETE, PERMISSION_DEPARTMENT_CREATE, PERMISSION_DEPARTMENT_EDIT,
    PERMISSION_DEPARTMENT_VIEW, PERMISSION_DEPARTMENT_DELETE)

link_agencies_menu = Link(text=_(u'agencies'), view='agency_list', icon=icon_agency)
link_agency_add = Link(text=_(u'create new agency'), view='agency_add', icon=icon_agency_add, permissions=[PERMISSION_AGENCY_CREATE])
link_agency_edit = Link(text=_(u'edit'), view='agency_edit', args='resolved_object.pk', icon=icon_agency_edit, permissions=[PERMISSION_AGENCY_EDIT])
link_agency_delete = Link(text=_('delete'), view='agency_delete', args='resolved_object.pk', icon=icon_agency_delete, permissions=[PERMISSION_AGENCY_DELETE])
link_agency_list = Link(text=_(u'agency list'), view='agency_list', icon=icon_agency, permissions=[PERMISSION_AGENCY_VIEW])

link_position_add = Link(text=_(u'create new position'), view='position_add', args='agency.pk', icon=icon_position_add, permissions=[PERMISSION_POSITION_CREATE])
link_position_edit = Link(text=_(u'edit'), view='position_edit', args='object.id', icon=icon_position_edit, permissions=[PERMISSION_POSITION_EDIT])
link_position_delete = Link(text=_('delete'), view='position_delete', args='object.id', icon=icon_position_delete, permissions=[PERMISSION_POSITION_DELETE])
link_position_list = Link(text=_(u'position list'), view='position_list', args='resolved_object.pk', icon=icon_position, permissions=[PERMISSION_POSITION_VIEW])

link_department_add = Link(text=_(u'create new department'), view='department_add', args='agency.pk', icon=icon_department_add, permissions=[PERMISSION_DEPARTMENT_CREATE])
link_department_edit = Link(text=_(u'edit'), view='department_edit', args='object.id', icon=icon_department_edit, permissions=[PERMISSION_DEPARTMENT_EDIT])
link_department_delete = Link(text=_('delete'), view='department_delete', args='object.id', icon=icon_department_delete, permissions=[PERMISSION_DEPARTMENT_DELETE])
link_department_list = Link(text=_(u'department list'), view='department_list', args='resolved_object.pk', icon=icon_department, permissions=[PERMISSION_DEPARTMENT_VIEW])
