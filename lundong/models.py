# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Bankuailundong(models.Model):
    num = models.IntegerField()
    value = models.FloatField()
    typ = models.CharField(max_length=30)