# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-18 11:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campus_ambassdor',
            name='phone',
            field=models.IntegerField(unique=True),
        ),
    ]