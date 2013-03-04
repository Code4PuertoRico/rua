# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'AgencyDepartment', fields ['label']
        db.delete_unique(u'agencies_agencydepartment', ['label'])

        # Removing unique constraint on 'AgencyPosition', fields ['label']
        db.delete_unique(u'agencies_agencyposition', ['label'])

        # Adding unique constraint on 'AgencyPosition', fields ['agency', 'label']
        db.create_unique(u'agencies_agencyposition', ['agency_id', 'label'])

        # Adding unique constraint on 'AgencyDepartment', fields ['agency', 'label']
        db.create_unique(u'agencies_agencydepartment', ['agency_id', 'label'])


    def backwards(self, orm):
        # Removing unique constraint on 'AgencyDepartment', fields ['agency', 'label']
        db.delete_unique(u'agencies_agencydepartment', ['agency_id', 'label'])

        # Removing unique constraint on 'AgencyPosition', fields ['agency', 'label']
        db.delete_unique(u'agencies_agencyposition', ['agency_id', 'label'])

        # Adding unique constraint on 'AgencyPosition', fields ['label']
        db.create_unique(u'agencies_agencyposition', ['label'])

        # Adding unique constraint on 'AgencyDepartment', fields ['label']
        db.create_unique(u'agencies_agencydepartment', ['label'])


    models = {
        u'agencies.agency': {
            'Meta': {'ordering': "['name']", 'object_name': 'Agency'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'registration': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'})
        },
        u'agencies.agencydepartment': {
            'Meta': {'ordering': "['label']", 'unique_together': "(['agency', 'label'],)", 'object_name': 'AgencyDepartment'},
            'agency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agencies.Agency']"}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
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