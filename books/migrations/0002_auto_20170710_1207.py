# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-10 12:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_pic',
            field=models.ImageField(upload_to=''),
        ),
    ]