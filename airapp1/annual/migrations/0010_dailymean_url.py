# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 05:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annual', '0009_dailymean'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailymean',
            name='url',
            field=models.CharField(default='', max_length=50),
        ),
    ]
