# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-05 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bankuailundong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('value', models.FloatField()),
                ('typ', models.CharField(max_length=30)),
            ],
        ),
    ]
