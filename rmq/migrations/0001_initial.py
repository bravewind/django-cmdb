# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-06-07 09:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Info_apply_rmq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rmq_name', models.CharField(max_length=100)),
                ('apply_time', models.DateTimeField()),
                ('rmq_vhost', models.CharField(max_length=20)),
                ('rmq_exchange', models.CharField(max_length=50)),
                ('rmq_comment', models.CharField(max_length=200)),
                ('rmq_product', models.CharField(max_length=20)),
                ('rmq_product_user', models.CharField(max_length=20)),
                ('rmq_consume', models.CharField(max_length=20)),
                ('rmq_consume_user', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Info_ip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_zone', models.CharField(choices=[(0, 'Aliyun'), (1, 'AWS'), (2, 'commany_inter')], max_length=1)),
                ('ip_addr', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='info_apply_rmq',
            name='info_ip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rmq.Info_ip'),
        ),
        migrations.AddField(
            model_name='info_apply_rmq',
            name='rmq_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
