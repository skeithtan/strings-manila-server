# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-31 11:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_administrator_nodes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='administrator_nodes',
            new_name='store_notes',
        ),
    ]
