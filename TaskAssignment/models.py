# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.db import models
# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=50)
    email = models.EmailField()

class Student(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=50)
    email = models.EmailField()

class Captain(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=50)
    email = models.EmailField()