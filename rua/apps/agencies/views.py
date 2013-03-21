from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib import messages
from django.core.urlresolvers import reverse

from permissions.models import Permission
from common.utils import generate_choices_w_labels, encapsulate
from common.widgets import two_state_template
from common.views import assign_remove

from .models import Agency, AgencyPosition
from .permissions import (PERMISSION_AGENCY_CREATE, PERMISSION_AGENCY_EDIT,
    PERMISSION_AGENCY_VIEW, PERMISSION_AGENCY_DELETE)
from .forms import AgencyForm, AgencyPositionForm
from .icons import icon_agency_delete, icon_position_delete


def agency_add(request):
    Permission.objects.check_permissions(request.user, [PERMISSION_AGENCY_CREATE])

    if request.method == 'POST':
        form = AgencyForm(request.POST)
        if form.is_valid():
            agency = form.save(commit=False)
            agency.set_unusable_password()
            agency.save()
            messages.success(request, _(u'Agency "%s" created successfully.') % agency)
            return HttpResponseRedirect(reverse('agency_set_password', args=[agency.pk]))
    else:
        form = AgencyForm()

    return render_to_response('generic_form.html', {
        'title': _(u'create new agency'),
        'form': form,
    },
    context_instance=RequestContext(request))


def agency_edit(request, agency_pk):
    Permission.objects.check_permissions(request.user, [PERMISSION_AGENCY_EDIT])
    agency = get_object_or_404(Agency, pk=agency_pk)

    if request.method == 'POST':
        form = AgencyForm(instance=agency, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _(u'Agency "%s" updated successfully.') % agency)
            return HttpResponseRedirect(reverse('agency_list'))
    else:
        form = AgencyForm(instance=agency)

    return render_to_response('generic_form.html', {
        'title': _(u'edit agency: %s') % agency,
        'form': form,
        'object': agency,
        'object_name': _(u'agency'),
    },
    context_instance=RequestContext(request))


def agency_delete(request, agency_pk=None, agency_pk_list=None):
    Permission.objects.check_permissions(request.user, [PERMISSION_AGENCY_DELETE])
    post_action_redirect = None

    if agency_pk:
        agencys = [get_object_or_404(Agency, pk=agency_pk)]
        post_action_redirect = reverse('agency_list')
    elif agency_pk_list:
        agencys = [get_object_or_404(Agency, pk=agency_pk) for agency_id in agency_pk_list.split(',')]
    else:
        messages.error(request, _(u'Must provide at least one agency.'))
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    previous = request.POST.get('previous', request.GET.get('previous', request.META.get('HTTP_REFERER', '/')))
    next = request.POST.get('next', request.GET.get('next', post_action_redirect if post_action_redirect else request.META.get('HTTP_REFERER', '/')))

    if request.method == 'POST':
        for agency in agencys:
            try:
                if agency.is_superagency or agency.is_staff:
                    messages.error(request, _(u'Super agency and staff agency deleting is not allowed, use the admin interface for these cases.'))
                else:
                    agency.delete()
                    messages.success(request, _(u'Agency "%s" deleted successfully.') % agency)
            except Exception, e:
                messages.error(request, _(u'Error deleting agency "%(agency)s": %(error)s') % {
                    'agency': agency, 'error': e
                })

        return HttpResponseRedirect(next)

    context = {
        'object_name': _(u'agency'),
        'delete_view': True,
        'previous': previous,
        'next': next,
        'form_icon': icon_agency_delete,
    }
    if len(agencys) == 1:
        context['object'] = agencys[0]
        context['title'] = _(u'Are you sure you wish to delete the agency: %s?') % ', '.join([unicode(d) for d in agencys])
    elif len(agencys) > 1:
        context['title'] = _(u'Are you sure you wish to delete the agencys: %s?') % ', '.join([unicode(d) for d in agencys])

    return render_to_response('generic_confirm.html', context,
        context_instance=RequestContext(request))


def agency_multiple_delete(request):
    return agency_delete(
        request, agency_pk_list=request.GET.get('id_list', [])
    )


def position_list(request, agency_pk):
    #Permission.objects.check_permissions(request.user, [PERMISSION_PERMISSION_GRANT, PERMISSION_PERMISSION_REVOKE])

    agency = get_object_or_404(Agency, pk=agency_pk)

    return render_to_response('generic_list.html', {
        'title': _(u'positions for agency: %s') % agency,
        'object_list': agency.positions,
        'agency': agency,
        'navigation_object_list': [
            {
                'object': 'agency',
            }
        ],
        'hide_link': True,
    }, context_instance=RequestContext(request))


def position_add(request, agency_pk):
    #Permission.objects.check_permissions(request.user, [PERMISSION_POSITION_CREATE])
    # TODO: add agency position add ACL

    agency = get_object_or_404(Agency, pk=agency_pk)

    if request.method == 'POST':
        form = AgencyPositionForm(request.POST)
        if form.is_valid():
            position = form.save(commit=False)
            position.agency = agency
            position.save()
            messages.success(request, _(u'Position "%s" created successfully.') % position)
            return HttpResponseRedirect(reverse('position_list', args=[agency.pk]))
    else:
        form = AgencyPositionForm()

    return render_to_response('generic_form.html', {
        'title': _(u'create new position for agency: %s') % agency,
        'form': form,
        'agency': agency,
        'navigation_object_list': [
            {
                'object': 'agency',
            }
        ],
    },
    context_instance=RequestContext(request))


def position_edit(request, position_pk):
    #Permission.objects.check_permissions(request.user, [PERMISSION_GROUP_EDIT])
    position = get_object_or_404(AgencyPosition, pk=position_pk)

    if request.method == 'POST':
        form = AgencyPositionForm(instance=position, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _(u'Position "%s" updated successfully.') % position)
            return HttpResponseRedirect(reverse('position_list', args=[position.agency.pk]))
    else:
        form = AgencyPositionForm(instance=position)

    return render_to_response('generic_form.html', {
        'title': _(u'edit position: %s') % position,
        'form': form,
        'object': position,
        'agency': position.agency,
        'navigation_object_list': [
            {
                'object': 'agency',
            }
        ],
        'object_name': _(u'position'),
    },
    context_instance=RequestContext(request))


def position_delete(request, position_pk=None, position_pk_list=None):
    #Permission.objects.check_permissions(request.user, [PERMISSION_POSITION_DELETE])
    post_action_redirect = None

    if position_pk:
        positions = [get_object_or_404(AgencyPosition, pk=position_pk)]
        post_action_redirect = reverse('position_list', args=[positions[0].agency.pk])
    elif position_pk_list:
        positions = [get_object_or_404(AgencyPosition, pk=position_pk) for position_id in position_pk_list.split(',')]
    else:
        messages.error(request, _(u'Must provide at least one position.'))
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    previous = request.POST.get('previous', request.GET.get('previous', request.META.get('HTTP_REFERER', reverse('home'))))
    next = request.POST.get('next', request.GET.get('next', post_action_redirect if post_action_redirect else request.META.get('HTTP_REFERER', reverse('home'))))

    if request.method == 'POST':
        for position in positions:
            try:
                position.delete()
                messages.success(request, _(u'Position "%s" deleted successfully.') % position)
            except Exception, e:
                messages.error(request, _(u'Error deleting position "%(position)s": %(error)s') % {
                    'position': position, 'error': e
                })

        return HttpResponseRedirect(next)

    context = {
        'object_name': _(u'position'),
        'agency': positions[0].agency,
        'delete_view': True,
        'previous': previous,
        'next': next,
        'form_icon': icon_position_delete,
    }
    if len(positions) == 1:
        context['object'] = positions[0]
        context['navigation_object_list'] = [
            {
                'object': 'agency',
            }
        ]
        context['title'] = _(u'Are you sure you wish to delete the position: %s?') % ', '.join([unicode(d) for d in positions])
    elif len(positions) > 1:
        context['title'] = _(u'Are you sure you wish to delete the positions: %s?') % ', '.join([unicode(d) for d in positions])

    return render_to_response('generic_confirm.html', context,
        context_instance=RequestContext(request))


def position_multiple_delete(request):
    return position_delete(
        request, position_pk_list=request.GET.get('id_list', [])
    )
