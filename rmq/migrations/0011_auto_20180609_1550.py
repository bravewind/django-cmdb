# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-06-09 07:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rmq', '0010_auto_20180609_1416'),
    ]

    operations = [
        migrations.RenameField(
            model_name='infoip',
            old_name='ip_addr',
            new_name='infoip',
        ),
    ]
