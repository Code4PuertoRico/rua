from django.core.urlresolvers import reverse
from django.contrib.auth.models import User, Group

from rest_framework import serializers

from agencies.models import (Agency, AgencyPosition, AgencyDepartment,
    DepartmentLocation, DepartmentEmployee)
from people.models import Person


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person


class AgencyPositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AgencyPosition


class DepartmentEmployeeSerializer(serializers.HyperlinkedModelSerializer):
    agency_position = AgencyPositionSerializer()
    person = PersonSerializer()

    class Meta:
        model = DepartmentEmployee


class DepartmentLocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DepartmentLocation


class AgencyDepartmentSerializer(serializers.HyperlinkedModelSerializer):
    locations = DepartmentLocationSerializer()
    employees = DepartmentEmployeeSerializer()

    class Meta:
        model = AgencyDepartment
        fields = ('url', 'label', 'start_date', 'end_date', 'locations', 'employees')


class AgencySerializer(serializers.HyperlinkedModelSerializer):
    positions = AgencyPositionSerializer()
    departments = AgencyDepartmentSerializer()

    class Meta:
        model = Agency
        fields = ('url', 'registration', 'name', 'positions', 'departments')
