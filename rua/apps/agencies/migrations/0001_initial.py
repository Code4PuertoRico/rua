# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table(u'agencies_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'agencies', ['Person'])

        # Adding model 'Agency'
        db.create_table(u'agencies_agency', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('registration', self.gf('django.db.models.fields.PositiveIntegerField')(unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('physical_address', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('postal_address', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('director', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['agencies.Person'], null=True, blank=True)),
        ))
        db.send_create_signal(u'agencies', ['Agency'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table(u'agencies_person')

        # Deleting model 'Agency'
        db.delete_table(u'agencies_agency')


    models = {
        u'agencies.agency': {
            'Meta': {'ordering': "['name']", 'object_name': 'Agency'},
            'director': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['agencies.Person']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'physical_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'postal_address': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'registration': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'})
        },
        u'agencies.person': {
            'Meta': {'object_name': 'Person'},
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['agencies']