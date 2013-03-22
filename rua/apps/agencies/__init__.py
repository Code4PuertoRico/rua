from __future__ import absolute_import

from django.contrib.auth.models import User, Group
from django.utils.translation import ugettext_lazy as _

from common.utils import encapsulate
from common.widgets import two_state_template
from navigation.api import (register_multi_item_links, register_model_list_columns,
    register_top_menu)
from navigation.classes import Link

from .links import (link_agencies_menu, link_agency_list, link_agency_add,
    link_agency_edit, link_agency_delete, link_position_add, link_position_delete,
    link_position_edit, link_position_list, link_department_add, link_department_delete,
    link_department_edit, link_department_list)
from .models import Agency, AgencyPosition, AgencyDepartment

Link.bind_links([Agency], [link_agency_edit, link_agency_delete, link_position_list, link_department_list])
Link.bind_links([Agency, 'agency_list', 'agency_add'], [link_agency_list, link_agency_add], menu_name=u'secondary_menu')

Link.bind_links([AgencyPosition, 'position_add', 'position_list'], [link_position_add], menu_name=u'sidebar')
Link.bind_links([AgencyPosition], [link_position_edit, link_position_delete])

Link.bind_links([AgencyDepartment, 'department_add', 'department_list'], [link_department_add], menu_name=u'sidebar')
Link.bind_links([AgencyDepartment], [link_department_edit, link_department_delete])

register_top_menu('agencies_menu', link=link_agencies_menu, position=2)

register_model_list_columns(AgencyDepartment, [
    {
        'name': _(u'main department?'),
        'attribute': encapsulate(lambda x: two_state_template(x.main_department).display_small())
    },
    {
        'name': _(u'creation date'),
        'attribute': 'start_date',
    },
    {
        'name': _(u'date disbanding'),
        'attribute': 'end_date',
    },
])
