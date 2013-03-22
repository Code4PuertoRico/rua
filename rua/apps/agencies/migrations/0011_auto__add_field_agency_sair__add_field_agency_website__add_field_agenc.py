# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Agency.sair'
        db.add_column(u'agencies_agency', 'sair',
                      self.gf('django.db.models.fields.PositiveIntegerField')(unique=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Agency.website'
        db.add_column(u'agencies_agency', 'website',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'Agency.organic_law'
        db.add_column(u'agencies_agency', 'organic_law',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


        # Changing field 'Agency.registration'
        db.alter_column(u'agencies_agency', 'registration', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True, null=True))

    def backwards(self, orm):
        # Deleting field 'Agency.sair'
        db.delete_column(u'agencies_agency', 'sair')

        # Deleting field 'Agency.website'
        db.delete_column(u'agencies_agency', 'website')

        # Deleting field 'Agency.organic_law'
        db.delete_column(u'agencies_agency', 'organic_law')


        # User chose to not deal with backwards NULL issues for 'Agency.registration'
        raise RuntimeError("Cannot reverse this migration. 'Agency.registration' and its values cannot be restored.")

    models = {
        u'agencies.agency': {
            'Meta': {'ordering': "['name']", 'object_name': 'Agency'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'organic_law': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'registration': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'sair': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'agencies.agencydepartment': {
            'Meta': {'ordering': "['label']", 'unique_together': "(['agency', 'label'],)", 'object_name': 'AgencyDepartment'},
            'agency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agencies.Agency']"}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'main_department': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'agencies.agencyposition': {
            'Meta': {'ordering': "['label']", 'unique_together': "(['agency', 'label'],)", 'object_name': 'AgencyPosition'},
            'agency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agencies.Agency']"}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'agencies.departmentemployee': {
            'Meta': {'ordering': "['agency_position']", 'object_name': 'DepartmentEmployee'},
            'agency_department': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'agency_department'", 'null': 'True', 'to': u"orm['agencies.AgencyDepartment']"}),
            'agency_position': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'agency_position'", 'to': u"orm['agencies.AgencyPosition']"}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'agency_person'", 'to': u"orm['people.Person']"}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'agencies.departmentlocation': {
            'Meta': {'ordering': "['start_date']", 'object_name': 'DepartmentLocation'},
            'agency_department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agencies.AgencyDepartment']"}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'physical_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'postal_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'people.person': {
            'Meta': {'object_name': 'Person'},
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['agencies']