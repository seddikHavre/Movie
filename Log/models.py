# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import UserManager

# Create your models here.

'''class Users(AbstractBaseUser, PermissionsMixin):

    class Meta:
        app_label = 'Log'
        db_table = "users"

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    username = models.CharField(max_length=20, unique=True)
    date_joined = models.DateField()
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        return self.first_name

    def get_short_name(self):
        return self.username

    def __unicode__(self):
        return self.email '''
