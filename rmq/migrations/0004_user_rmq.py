# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-06-07 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rmq', '0003_auto_20180607_1800'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_rmq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]