# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DepartmentLocation'
        db.create_table(u'agencies_departmentlocation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('agency_department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['agencies.AgencyDepartment'])),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('physical_address', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('postal_address', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('longitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'agencies', ['DepartmentLocation'])

        # Adding model 'AgencyPosition'
        db.create_table(u'agencies_agencyposition', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('agency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['agencies.Agency'])),
            ('label', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
        ))
        db.send_create_signal(u'agencies', ['AgencyPosition'])

        # Adding model 'AgencyEmployee'
        db.create_table(u'agencies_agencyemployee', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('agency_position', self.gf('django.db.models.fields.related.ForeignKey')(related_name='agency_position', to=orm['agencies.AgencyPosition'])),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(related_name='agency_person', to=orm['agencies.AgencyPosition'])),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
        ))
        db.send_create_signal(u'agencies', ['AgencyEmployee'])

        # Adding model 'AgencyDepartment'
        db.create_table(u'agencies_agencydepartment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('agency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['agencies.Agency'])),
            ('label', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
        ))
        db.send_create_signal(u'agencies', ['AgencyDepartment'])

        # Deleting field 'Agency.physical_address'
        db.delete_column(u'agencies_agency', 'physical_address')

        # Deleting field 'Agency.postal_address'
        db.delete_column(u'agencies_agency', 'postal_address')

        # Deleting field 'Agency.director'
        db.delete_column(u'agencies_agency', 'director_id')


    def backwards(self, orm):
        # Deleting model 'DepartmentLocation'
        db.delete_table(u'agencies_departmentlocation')

        # Deleting model 'AgencyPosition'
        db.delete_table(u'agencies_agencyposition')

        # Deleting model 'AgencyEmployee'
        db.delete_table(u'agencies_agencyemployee')

        # Deleting model 'AgencyDepartment'
        db.delete_table(u'agencies_agencydepartment')

        # Adding field 'Agency.physical_address'
        db.add_column(u'agencies_agency', 'physical_address',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Agency.postal_address'
        db.add_column(u'agencies_agency', 'postal_address',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'Agency.director'
        db.add_column(u'agencies_agency', 'director',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['people.Person'], null=True, blank=True),
                      keep_default=False)


    models = {
        u'agencies.agency': {
            'Meta': {'ordering': "['name']", 'object_name': 'Agency'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'registration': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'})
        },
        u'agencies.agencydepartment': {
            'Meta': {'ordering': "['label']", 'object_name': 'AgencyDepartment'},
            'agency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agencies.Agency']"}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'})
        },
        u'agencies.agencyemployee': {
            'Meta': {'ordering': "['agency_position']", 'object_name': 'AgencyEmployee'},
            'agency_position': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'agency_position'", 'to': u"orm['agencies.AgencyPosition']"}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'agency_person'", 'to': u"orm['agencies.AgencyPosition']"}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'})
        },
        u'agencies.agencyposition': {
            'Meta': {'ordering': "['label']", 'object_name': 'AgencyPosition'},
            'agency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agencies.Agency']"}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'})
        },
        u'agencies.departmentlocation': {
            'Meta': {'ordering': "['start_date']", 'object_name': 'DepartmentLocation'},
            'agency_department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agencies.AgencyDepartment']"}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'physical_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'postal_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['agencies']