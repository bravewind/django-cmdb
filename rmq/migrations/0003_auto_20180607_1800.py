# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-06-07 10:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rmq', '0002_auto_20180607_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info_ip',
            name='ip_zone',
            field=models.CharField(choices=[('aliyun', 'Aliyun'), ('AWS', 'AWS'), ('commany_inter', 'commany_inter')], max_length=10),
        ),
    ]