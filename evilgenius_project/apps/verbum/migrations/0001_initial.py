# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Bloggable'
        db.create_table('verbum_bloggable', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('model_utils.fields.StatusField')(default='draft', max_length=100, no_check_for_status=True)),
            ('when', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=250, db_index=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('verbum', ['Bloggable'])

        # Adding model 'Post'
        db.create_table('verbum_post', (
            ('bloggable_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['verbum.Bloggable'], unique=True, primary_key=True)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('excerpt', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('verbum', ['Post'])

        # Adding model 'Link'
        db.create_table('verbum_link', (
            ('bloggable_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['verbum.Bloggable'], unique=True, primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=250)),
        ))
        db.send_create_signal('verbum', ['Link'])


    def backwards(self, orm):
        
        # Deleting model 'Bloggable'
        db.delete_table('verbum_bloggable')

        # Deleting model 'Post'
        db.delete_table('verbum_post')

        # Deleting model 'Link'
        db.delete_table('verbum_link')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'verbum.bloggable': {
            'Meta': {'ordering': "['when', 'title']", 'object_name': 'Bloggable'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '250', 'db_index': 'True'}),
            'status': ('model_utils.fields.StatusField', [], {'default': "'draft'", 'max_length': '100', 'no_check_for_status': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'when': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        },
        'verbum.link': {
            'Meta': {'ordering': "['when', 'title']", 'object_name': 'Link', '_ormbases': ['verbum.Bloggable']},
            'bloggable_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['verbum.Bloggable']", 'unique': 'True', 'primary_key': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '250'})
        },
        'verbum.post': {
            'Meta': {'ordering': "['when', 'title']", 'object_name': 'Post', '_ormbases': ['verbum.Bloggable']},
            'bloggable_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['verbum.Bloggable']", 'unique': 'True', 'primary_key': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'excerpt': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['verbum']
