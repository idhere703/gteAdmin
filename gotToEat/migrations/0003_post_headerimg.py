# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-16 22:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gotToEat', '0002_auto_20170506_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='headerImg',
            field=models.FileField(default=django.utils.timezone.now, upload_to='uploads/'),
            preserve_default=False,
        ),
    ]
