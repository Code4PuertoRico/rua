from django.db import models
from django.utils.translation import ugettext_lazy as _

from people.models import Person

#TODO: Add agency logo model

class Agency(models.Model):
    registration = models.PositiveIntegerField(verbose_name=_(u'registration'), unique=True)
    name = models.CharField(max_length=128, verbose_name=_(u'name'), unique=True)

    # TODO: add website
    # TODO: add organic law link/text

    def __unicode__(self):
        return self.name

    def natural_key(self):
        return (self.registration,)

    @property
    def positions(self):
        return self.agencyposition_set.all()

    @property
    def departments(self):
        return self.agencydepartment_set.all()

    @property
    def employees(self):
        return AgencyEmployee.objects.filter(agency_department__agency=self)

    class Meta:
        verbose_name = _(u'agency')
        verbose_name_plural = _(u'agencies')
        ordering = ['name']


class AgencyPosition(models.Model):
    agency = models.ForeignKey(Agency, verbose_name=_(u'agency'))
    label = models.CharField(max_length=128, verbose_name=_(u'name'), unique=True)
    start_date = models.DateField(verbose_name=_(u'start date'), null=True, blank=True)
    end_date = models.DateField(verbose_name=_(u'start date'), null=True, blank=True)

    def __unicode__(self):
        return self.label

    def natural_key(self):
        return (self.agency, self.label, )
    
    class Meta:
        verbose_name = _(u'position')
        verbose_name_plural = _(u'positions')
        #ordering = ['label']


class AgencyDepartment(models.Model):
    agency = models.ForeignKey(Agency, verbose_name=_(u'agency'))
    label = models.CharField(max_length=128, verbose_name=_(u'name'), unique=True)
    start_date = models.DateField(verbose_name=_(u'start date'), null=True, blank=True)
    end_date = models.DateField(verbose_name=_(u'end date'), null=True, blank=True)

    @property
    def employees(self):
        return self.agencyemployee_set.all()

    @property
    def locations(self):
        return self.departmentlocation_set.all()

    def __unicode__(self):
        return self.label

    def natural_key(self):
        return (self.agency, self.label, )

    class Meta:
        verbose_name = _(u'department')
        verbose_name_plural = _(u'departments')
        ordering = ['label']


class DepartmentEmployee(models.Model):
    agency_department = models.ForeignKey(AgencyDepartment, related_name='agency_department', verbose_name=_(u'agency department'), null=True, blank=True)
    agency_position = models.ForeignKey(AgencyPosition, related_name='agency_position', verbose_name=_(u'agency position'))
    person = models.ForeignKey(Person, related_name='agency_person', verbose_name=_(u'person'))
    start_date = models.DateField(verbose_name=_(u'start date'), null=True, blank=True)
    end_date = models.DateField(verbose_name=_(u'end date'), null=True, blank=True)
    # TODO: add phone number + extension

    def __unicode__(self):
        return unicode(self.person)

    def natural_key(self):
        return (self.agency_department, self.agency_position, self.person)

    class Meta:
        verbose_name = _(u'employee')
        verbose_name_plural = _(u'employees')
        ordering = ['agency_position']    


class DepartmentLocation(models.Model):
    agency_department = models.ForeignKey(AgencyDepartment, verbose_name=_(u'agency department'))
    start_date = models.DateField(verbose_name=_(u'start date'), null=True, blank=True)
    end_date = models.DateField(verbose_name=_(u'end date'), null=True, blank=True)
    # TODO: add phone number + extension

    # TODO: switch to module address scheme
    physical_address = models.TextField(verbose_name=_(u'physical address'), blank=True)
    postal_address = models.TextField(verbose_name=_(u'postal address'), blank=True)

    # TODO: Switch to GeoDjango PointField field type
    latitude = models.FloatField(_(u'latitude'), blank=True, null=True)
    longitude = models.FloatField(_(u'longitude'), blank=True, null=True)    

    def __unicode__(self):
        return unicode(self.agency_department)

    class Meta:
        verbose_name = _(u'department location')
        verbose_name_plural = _(u'department locations')
        ordering = ['start_date']
