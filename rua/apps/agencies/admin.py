from __future__ import absolute_import

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Agency


admin.site.register(Agency)
