from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from navigation.classes import Link

from .icons import (icon_agency, icon_agency_add, icon_agency_edit, icon_agency_delete)
from .permissions import (PERMISSION_AGENCY_CREATE, PERMISSION_AGENCY_EDIT,
    PERMISSION_AGENCY_VIEW, PERMISSION_AGENCY_DELETE)

link_agencies_menu = Link(text=_(u'agencies'), view='agency_list', icon=icon_agency)
link_agency_add = Link(text=_(u'create new agency'), view='agency_add', icon=icon_agency_add, permissions=[PERMISSION_AGENCY_CREATE])
link_agency_edit = Link(text=_(u'edit'), view='agency_edit', args='object.id', icon=icon_agency_edit, permissions=[PERMISSION_AGENCY_EDIT])
link_agency_delete = Link(text=_('delete'), view='agency_delete', args='object.id', icon=icon_agency_delete, permissions=[PERMISSION_AGENCY_DELETE])
link_agency_list = Link(text=_(u'agency list'), view='agency_list', icon=icon_agency, permissions=[PERMISSION_AGENCY_VIEW])
