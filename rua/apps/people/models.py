from django.db import models
from django.utils.translation import ugettext_lazy as _


class Person(models.Model):
    full_name = models.CharField(max_length=128, verbose_name=_(u'full name'))

    def __unicode__(self):
        return self.full_name

    class Meta:
        verbose_name = _(u'person')
        verbose_name_plural = _(u'people')
