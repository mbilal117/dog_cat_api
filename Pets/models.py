# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User as Django_User
# Create your models here.
class Pets(models.Model):
    TYPE = (
        ("1", 'DOG'),
        ("2", 'CAT'),
    )
    owner = models.ForeignKey(Django_User)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=1, default=1, choices=TYPE)
    dob = models.DateField()
    def __str__(self):
        return self.name
