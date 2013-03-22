from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from permissions.models import PermissionNamespace, Permission

namespace = PermissionNamespace('agencies', _(u'Agencies'))

PERMISSION_AGENCY_CREATE = Permission.objects.register(namespace, 'agency_create', _(u'Create new agency'))
PERMISSION_AGENCY_EDIT = Permission.objects.register(namespace, 'agency_edit', _(u'Edit existing agency'))
PERMISSION_AGENCY_VIEW = Permission.objects.register(namespace, 'agency_view', _(u'View existing agency'))
PERMISSION_AGENCY_DELETE = Permission.objects.register(namespace, 'agency_delete', _(u'Delete existing agency'))

PERMISSION_POSITION_CREATE = Permission.objects.register(namespace, 'position_create', _(u'Create new position'))
PERMISSION_POSITION_EDIT = Permission.objects.register(namespace, 'position_edit', _(u'Edit existing position'))
PERMISSION_POSITION_VIEW = Permission.objects.register(namespace, 'position_view', _(u'View existing position'))
PERMISSION_POSITION_DELETE = Permission.objects.register(namespace, 'position_delete', _(u'Delete existing position'))

PERMISSION_DEPARTMENT_CREATE = Permission.objects.register(namespace, 'department_create', _(u'Create new department'))
PERMISSION_DEPARTMENT_EDIT = Permission.objects.register(namespace, 'department_edit', _(u'Edit existing department'))
PERMISSION_DEPARTMENT_VIEW = Permission.objects.register(namespace, 'department_view', _(u'View existing department'))
PERMISSION_DEPARTMENT_DELETE = Permission.objects.register(namespace, 'department_delete', _(u'Delete existing department'))
