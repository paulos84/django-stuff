# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 08:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('annual', '0005_auto_20170202_1539'),
    ]

    operations = [
        migrations.RenameField(
            model_name='annualmean',
            old_name='slug',
            new_name='url',
        ),
    ]
