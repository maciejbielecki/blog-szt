# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-07 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='kategoria', max_length=200),
        ),
    ]