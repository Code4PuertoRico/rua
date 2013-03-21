from __future__ import absolute_import

from django.contrib.auth.models import User, Group
from django.utils.translation import ugettext_lazy as _

from common.utils import encapsulate
#from common.widgets import two_state_template
from navigation.api import (register_multi_item_links, register_model_list_columns,
    register_top_menu)
from navigation.classes import Link
#from project_setup.api import register_setup

from .links import (link_agencies_menu, link_agency_list, link_agency_add,
    link_agency_edit, link_agency_delete)
from .models import Agency

Link.bind_links([Agency], [link_agency_edit, link_agency_delete])
Link.bind_links([Agency, 'agency_list', 'agency_add'], [link_agency_list, link_agency_add], menu_name=u'secondary_menu')
#register_multi_item_links(['user_list'], [user_multiple_set_password, user_multiple_delete])
register_top_menu('agencies_menu', link=link_agencies_menu, position=2)
