# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-10 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userdialog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=50)),
                ('lasttime', models.IntegerField()),
                ('tulingflag', models.IntegerField()),
                ('jokingstep', models.IntegerField()),
            ],
        ),
    ]