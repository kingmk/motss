import datetime
from django.utils import timezone
from django.db import models
import json



def default_subscribe():
    subs = ['tag1', 'tag2', 'tag3']
    return json.dumps(subs)

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
    subscribetag = models.TextField(null=True, default=default_subscribe())

    loginip = ''

    @classmethod
    def create(cls, username, password, email, loginip) :
        member = Member(username=username, password=password, email=email)
        member.loginip = loginip
        return member


    def __unicode__(self):
    	return 'username:'+str(self.username)+', email:'+str(self.email)+\
        ', subscribetag:'+str(self.subscribetag)

    def subscribed_tags(self):
        return json.loads(self.subscribetag)


