# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Company'
        db.create_table(u'mentors_company', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'mentors', ['Company'])

        # Adding model 'Industry'
        db.create_table(u'mentors_industry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'mentors', ['Industry'])

        # Adding model 'Degree'
        db.create_table(u'mentors_degree', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'mentors', ['Degree'])

        # Adding model 'Mentor'
        db.create_table(u'mentors_mentor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(related_name='mentors', to=orm['mentors.Company'])),
            ('industry', self.gf('django.db.models.fields.related.ForeignKey')(related_name='mentors', to=orm['mentors.Industry'])),
            ('degree', self.gf('django.db.models.fields.related.ForeignKey')(related_name='mentors', to=orm['mentors.Degree'])),
        ))
        db.send_create_signal(u'mentors', ['Mentor'])


    def backwards(self, orm):
        # Deleting model 'Company'
        db.delete_table(u'mentors_company')

        # Deleting model 'Industry'
        db.delete_table(u'mentors_industry')

        # Deleting model 'Degree'
        db.delete_table(u'mentors_degree')

        # Deleting model 'Mentor'
        db.delete_table(u'mentors_mentor')


    models = {
        u'mentors.company': {
            'Meta': {'object_name': 'Company'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'mentors.degree': {
            'Meta': {'object_name': 'Degree'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'mentors.industry': {
            'Meta': {'object_name': 'Industry'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'mentors.mentor': {
            'Meta': {'object_name': 'Mentor'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mentors'", 'to': u"orm['mentors.Company']"}),
            'degree': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mentors'", 'to': u"orm['mentors.Degree']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'mentors'", 'to': u"orm['mentors.Industry']"}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['mentors']