# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class users(models.Model):
    first_name = models.CharField(max_length=20,null = False)
    last_name = models.CharField(max_length=20, null=False)
    user_name = models.CharField(max_length=20,null = False)
    Email = models.CharField(max_length=30,null = False)
    password = models.CharField(max_length=20,null = False)


    def __str__(self):
        return "{0}, {1}".format(self.user_name, self.first_name)


