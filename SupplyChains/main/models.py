# from __future__ import unicode_literals
from django.db import models


import re
import uuid
# from django.contrib.postgres.fields import ArrayField
from django.core import validators
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django import forms
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# from djangotoolbox import *
# from djangotoolbox.fields import ListField
# Create your models here.


class Attr(models.Model):
    Attri = models.CharField(null=False, max_length=30)
    Period = models.IntegerField()
    Value = models.DecimalField(max_digits=15, decimal_places=4, null=False)

    class Meta:
        unique_together = ["Attri", "Period"]


class Para(models.Model):
    Username = models.CharField(null=False, max_length=30)
    Param = models.CharField(null=False, max_length=30)
    Period = models.IntegerField()
    Value = models.DecimalField(max_digits=15, decimal_places=4, null=False)


    # date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    # last_activity = models.DateTimeField(blank=True, null=True)

    # objects = UserManager()

    # USERNAME_FIELD = 'username'
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Para._meta.fields]
    class Meta:
        unique_together = ["Username", "Param", "Period"]

class UserUtil(models.Model):
    Username=models.CharField(null=False,max_length=30)
    last_activity= models.DateTimeField(blank=True, null=True)
    # info_profitgraph = ArrayField(models.IntegerField(),blank=True)
    class Meta:
        unique_together = ["Username"]
    # last_login=models.DateTimeField(blank=True, null=True)


class UserGraphUtil(models.Model):
    Username=models.CharField(null=False,max_length=30)
    graph_mode=models.IntegerField()
    profit_vals=models.CharField(null=True,max_length=255)
    # profit_vals=models.DecimalField(max_digits=15, decimal_places=4,null=True)

    class Meta:
        unique_together = ["Username","graph_mode"]


