# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-06-08 06:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rmq', '0005_auto_20180608_1402'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Users',
        ),
    ]