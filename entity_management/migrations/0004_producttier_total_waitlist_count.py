# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-28 02:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entity_management', '0003_auto_20170824_0334'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttier',
            name='total_waitlist_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
