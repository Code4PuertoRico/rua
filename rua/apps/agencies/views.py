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

from .models import Agency
from .permissions import (PERMISSION_AGENCY_CREATE, PERMISSION_AGENCY_EDIT,
    PERMISSION_AGENCY_VIEW, PERMISSION_AGENCY_DELETE)
from .forms import AgencyForm
from .icons import icon_agency_delete


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
