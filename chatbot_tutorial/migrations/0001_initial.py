# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2021-11-01 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(blank=True, null=True)),
                ('stupid', models.IntegerField(blank=True, null=True)),
                ('fat', models.IntegerField(blank=True, null=True)),
                ('dumb', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
