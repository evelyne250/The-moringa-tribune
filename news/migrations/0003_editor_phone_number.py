# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-10-08 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20191008_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='editor',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
