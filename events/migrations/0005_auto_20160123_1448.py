# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-23 19:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20160123_1322'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='date',
            new_name='start_date',
        ),
    ]
