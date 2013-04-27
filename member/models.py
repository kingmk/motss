import datetime
from django.utils import timezone
from django.db import models
from django.db.models import F
from django.contrib.auth.models import AbstractUser
import json

DEFAULT_AVATAR = '/statics/images/default_avartar.png'

class MotssUser(AbstractUser):
    avatarurl = models.CharField(max_length=250, default=DEFAULT_AVATAR)
    follow_count = models.IntegerField(default=0, db_index=True)
    follower_count = models.IntegerField(default=0, db_index=True)
    loginip = ''

    @classmethod
    def create(cls, username, password, email, loginip) :
        user = MotssUser(username=username, email=email)
        user.set_password(password)
        user.loginip = loginip
        return user

    def __unicode__(self):
        s = 'id:'+str(self.id)
        s += ', username:'+str(self.username)
        s += ', password:'+str(self.password)
        s += ', email:'+str(self.email)
        s += ', is_superuser:'+str(self.is_superuser)
        s += ', is_staff:'+str(self.is_staff)
        s += ', is_active:'+str(self.is_active)
        s += ', date_joined:'+str(self.date_joined)
        s += ', last_login:'+str(self.last_login)
        s += ', avatarurl:'+str(self.avatarurl)
        return s

    def inc_follow(self, count):
        self.follow_count = F('follow_count')+count
        self.save(update_fields=['follow_count'])

    def inc_follower(self, count):
        self.follower_count = F('follower_count')+count
        self.save(update_fields=['follower_count'])

class MotssProfile(models.Model):
    user = models.OneToOneField(MotssUser)
    birthday = models.DateTimeField()
    gender = models.SmallIntegerField(default=0, db_index=True)

class MotssFollow(models.Model):
    user = models.ForeignKey(MotssUser, related_name='follower')
    follow = models.ForeignKey(MotssUser, related_name='follow')
    createtime = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "follow")

    def __unicode__(self):
        s = 'id:'+str(self.id)
        s += ', user_id:'+str(self.user_id)
        s += ', follow_id:'+str(self.follow_id)
        s += ', createtime:'+str(self.createtime)
        return s

def default_subscribe():
    subs = ['tag1', 'tag2', 'tag3']
    return json.dumps(subs)

