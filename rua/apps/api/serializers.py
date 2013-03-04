from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group

from rest_framework import serializers

from agencies.models import (Agency, AgencyPosition, AgencyDepartment,
    DepartmentLocation)


class DepartmentLocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DepartmentLocation
        fields = ('start_date', 'end_date', 'physical_address', 'postal_address', 'latitude', 'longitude')


class AgencyPositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AgencyPosition
        fields = ('label', 'start_date', 'end_date')


class AgencyDepartmentSerializer(serializers.HyperlinkedModelSerializer):
    locations = DepartmentLocationSerializer()

    class Meta:
        model = AgencyDepartment
        fields = ('label', 'start_date', 'end_date', 'locations')


class AgencySerializer(serializers.HyperlinkedModelSerializer):
    positions = AgencyPositionSerializer()
    departments = AgencyDepartmentSerializer()

    class Meta:
        model = Agency
        fields = ('url', 'registration', 'name', 'positions', 'departments')


