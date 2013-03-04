from __future__ import absolute_import

import logging

from django.contrib.auth.models import User, Group

from rest_framework import generics
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from agencies.models import (Agency, AgencyPosition, AgencyDepartment,
	DepartmentLocation, DepartmentEmployee)
from people.models import Person

from .serializers import (AgencySerializer, AgencyPositionSerializer,
	AgencyDepartmentSerializer, DepartmentLocationSerializer,
	DepartmentEmployeeSerializer, PersonSerializer)

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
        'people': reverse('person-list', request=request),
    })


class AgencyList(generics.ListAPIView):
    model = Agency
    serializer_class = AgencySerializer


class AgencyDetail(generics.RetrieveAPIView):
    model = Agency
    serializer_class = AgencySerializer


class AgencyPositionDetail(generics.RetrieveAPIView):
    model = AgencyPosition
    serializer_class = AgencyPositionSerializer


class AgencyDepartmentDetail(generics.RetrieveAPIView):
    model = AgencyDepartment
    serializer_class = AgencyDepartmentSerializer


class DepartmentLocationDetail(generics.RetrieveAPIView):
    model = DepartmentLocation
    serializer_class = DepartmentLocationSerializer


class DepartmentEmployeeDetail(generics.RetrieveAPIView):
    model = DepartmentEmployee
    serializer_class = DepartmentEmployeeSerializer


class PersonList(generics.ListAPIView):
    model = Person
    serializer_class = PersonSerializer


class PersonDetail(generics.RetrieveAPIView):
    model = Person
    serializer_class = PersonSerializer
