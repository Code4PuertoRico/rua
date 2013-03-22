from __future__ import absolute_import

from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Agency, AgencyPosition, AgencyDepartment


class AgencyForm(forms.ModelForm):
    class Meta:
        model = Agency


class AgencyPositionForm(forms.ModelForm):
    class Meta:
        model = AgencyPosition
        exclude = 'agency'


class AgencyDepartmentForm(forms.ModelForm):
    class Meta:
        model = AgencyDepartment
        exclude = 'agency'
