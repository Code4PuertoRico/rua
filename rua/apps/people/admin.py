from __future__ import absolute_import

from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.utils.translation import ugettext_lazy as _

from .models import Person

admin.site.register(Person)
