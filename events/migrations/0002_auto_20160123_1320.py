# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-23 18:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='start_date',
            new_name='date',
        ),
        migrations.AddField(
            model_name='event',
            name='organizer',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='organizer', to='main.TeamMember'),
        ),
    ]
