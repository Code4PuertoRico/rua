from __future__ import absolute_import

from django.contrib.auth.models import User, Group
from django.utils.translation import ugettext_lazy as _

from common.utils import encapsulate
from common.widgets import two_state_template
from navigation.api import register_multi_item_links, register_model_list_columns
from navigation.classes import Link
from project_setup.api import register_setup

from .links import (user_list, user_setup, user_edit, user_add, user_delete,
    user_multiple_delete, user_set_password, user_multiple_set_password,
    user_groups, group_list, group_setup, group_edit, group_add,
    group_delete, group_multiple_delete, group_members)

Link.bind_links([User], [user_edit, user_set_password, user_groups, user_delete])
Link.bind_links([User, 'user_multiple_set_password', 'user_multiple_delete', 'user_list', 'user_add'], [user_list, user_add], menu_name=u'secondary_menu')
register_multi_item_links(['user_list'], [user_multiple_set_password, user_multiple_delete])

Link.bind_links([Group], [group_edit, group_members, group_delete])
Link.bind_links(['group_multiple_delete', 'group_delete', 'group_edit', 'group_list', 'group_add', 'group_members'], [group_list, group_add], menu_name=u'secondary_menu')
register_multi_item_links(['group_list'], [group_multiple_delete])

user_management_views = [
    'user_list', 'user_edit', 'user_add', 'user_delete',
    'user_multiple_delete', 'user_set_password',
    'user_multiple_set_password', 'group_list', 'group_edit', 'group_add',
    'group_delete', 'group_multiple_delete', 'group_members'
]

register_setup(user_setup)
register_setup(group_setup)

register_model_list_columns(User, [
    {
        'name': _(u'full name'),
        'attribute': 'get_full_name'
    },
    {
        'name': _(u'email'),
        'attribute': 'email'
    },
    {
        'name': _(u'active'),
        'attribute': encapsulate(lambda x: two_state_template(x.is_active).display_small()),
    },
    {
        'name': _(u'has usable password?'),
        'attribute': encapsulate(lambda x: two_state_template(x.has_usable_password()).display_small()),
    },
])

register_model_list_columns(Group, [
    {
        'name': _(u'members'),
        'attribute': 'user_set.count'
    },
])
