# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 20:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b20', '0004_auto_20161101_0221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='deviceid',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='mobileno',
            field=models.BigIntegerField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='socialid',
            field=models.BigIntegerField(),
        ),
    ]
