# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-06-12 13:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rmq', '0012_users_u_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='info_apply_rmq',
            name='rmq_status',
            field=models.IntegerField(default=0, max_length=1),
        ),
    ]
