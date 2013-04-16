import datetime
from django.utils import timezone
from django.db import models


class Member(models.Model):
    uid = models.AutoField(primary_key=True)
    email = models.EmailField()
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=32)
    status = models.SmallIntegerField(default=0, db_index=True)
    emailstatus = models.SmallIntegerField(default=0)
    avatarstatus = models.SmallIntegerField(default=0)
    adminid = models.SmallIntegerField(default=0)
    groupid = models.SmallIntegerField(default=0)
    regdate = models.DateTimeField(auto_now_add=True)

    loginip = ''

    def __unicode__(self):
    	return self.username+self.email
