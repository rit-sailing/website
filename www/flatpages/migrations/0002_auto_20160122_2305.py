# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-23 04:05
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flatpages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flatpage',
            name='content',
        ),
        migrations.AddField(
            model_name='flatpage',
            name='ccontent',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='stuff'),
            preserve_default=False,
        ),
    ]