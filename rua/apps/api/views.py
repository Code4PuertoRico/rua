from __future__ import absolute_import

import logging

from django.contrib.auth.models import User, Group

from rest_framework import generics
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from agencies.models import Agency

from .serializers import AgencySerializer

logger = logging.getLogger(__name__)


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'v0': reverse('api-version-0', request=request),
    })


@api_view(('GET',))
def version_0(request, format=None):
    return Response({
        'agencies': reverse('agency-list', request=request),
    })

class AgencyList(generics.ListCreateAPIView):
    model = Agency
    serializer_class = AgencySerializer


class AgencyDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Agency
    serializer_class = AgencySerializer
