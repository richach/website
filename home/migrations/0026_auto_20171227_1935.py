# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-27 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_auto_20171227_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Community URL slug: https://www.outreachy.org/communities/SLUG/'),
        ),
    ]