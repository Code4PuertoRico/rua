from django.db import models
from django.utils.translation import ugettext_lazy as _


class Agency(models.Model):
	# Direct properties
    registration = models.PositiveIntegerField(verbose_name=_(u'registration'), unique=True)
    name = models.CharField(max_length=128, verbose_name=_(u'name'), unique=True)
    
    # Physical properties
    physical_address = models.TextField(verbose_name=_(u'physical address'), blank=True)
    postal_address = models.TextField(verbose_name=_(u'postal address'), blank=True)

    objects = OmitDisabledManager()

    def __unicode__(self):
        return self.name

    def natural_key(self):
        return (self.registration,)

    class Meta:
        verbose_name = _(u'agency')
        verbose_name_plural = _(u'agencies')
        ordering = ['name']
