# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-05 22:51
from __future__ import unicode_literals

from django.db import migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('yellow_line', '0010_auto_20161206_0338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='event_position',
            field=geoposition.fields.GeopositionField(default=geoposition.fields.GeopositionField(max_length=42, verbose_name=28.6139391), max_length=42),
        ),
    ]
