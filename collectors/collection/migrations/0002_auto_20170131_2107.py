# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-31 21:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='subtype',
        ),
        migrations.RemoveField(
            model_name='collectionsubtype',
            name='type',
        ),
        migrations.AddField(
            model_name='category',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collection.CollectionType', verbose_name='Type'),
        ),
        migrations.AddField(
            model_name='collectiontype',
            name='subtype',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='collection.CollectionSubType', verbose_name='Subtype'),
        ),
    ]
