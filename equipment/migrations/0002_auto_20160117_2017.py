# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-18 01:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Request',
            new_name='ItemRequest',
        ),
    ]
