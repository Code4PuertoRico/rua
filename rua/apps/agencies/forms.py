from __future__ import absolute_import

from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import Agency, AgencyPosition


class AgencyForm(forms.ModelForm):
    class Meta:
        model = Agency


class AgencyPositionForm(forms.ModelForm):
    class Meta:
        model = AgencyPosition
        exclude = 'agency'
