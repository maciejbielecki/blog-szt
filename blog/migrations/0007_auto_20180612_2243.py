# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-12 20:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20180611_1408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='active',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='employee_name',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='short_name',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='login_date_last',
            field=models.DateTimeField(default=None),
        ),
    ]
