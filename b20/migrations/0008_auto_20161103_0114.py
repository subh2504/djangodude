# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b20', '0007_auto_20161103_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alivevoucher',
            name='couponcode',
            field=models.TextField(unique=True),
        ),
    ]
