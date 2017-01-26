# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-22 18:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collectionsubtype',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True, default=datetime.datetime(2017, 1, 22, 18, 27, 21, 332379, tzinfo=utc), verbose_name='Data stworzenia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collectionsubtype',
            name='modified',
            field=models.DateTimeField(auto_now=True, db_index=True, default=datetime.datetime(2017, 1, 22, 18, 27, 26, 205660, tzinfo=utc), verbose_name='Data modyfikacji'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collectiontype',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True, default=datetime.datetime(2017, 1, 22, 18, 27, 34, 348008, tzinfo=utc), verbose_name='Data stworzenia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collectiontype',
            name='modified',
            field=models.DateTimeField(auto_now=True, db_index=True, default=datetime.datetime(2017, 1, 22, 18, 27, 37, 702256, tzinfo=utc), verbose_name='Data modyfikacji'),
            preserve_default=False,
        ),
    ]