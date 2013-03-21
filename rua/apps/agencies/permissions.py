from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _

from permissions.models import PermissionNamespace, Permission

namespace = PermissionNamespace('agencies', _(u'Agencies'))

PERMISSION_AGENCY_CREATE = Permission.objects.register(namespace, 'agency_create', _(u'Create new agency'))
PERMISSION_AGENCY_EDIT = Permission.objects.register(namespace, 'agency_edit', _(u'Edit existing agency'))
PERMISSION_AGENCY_VIEW = Permission.objects.register(namespace, 'agency_view', _(u'View existing agency'))
PERMISSION_AGENCY_DELETE = Permission.objects.register(namespace, 'agency_delete', _(u'Delete existing agency'))
