import datetime
from django.utils import timezone
from django.db import models
from django.db.models import Q

class Message (models.Model):
    mid = models.AutoField(primary_key=True)
    cid = models.SmallIntegerField(default=0)
    sender = models.SmallIntegerField(default=0)
    content = models.CharField(max_length=300)
    send_time = models.DateTimeField(auto_now_add=True)    
    def __unicode__(self):
        return self.content

class Chat (models.Model):
    cid = models.AutoField(primary_key=True)
    uid1 = models.IntegerField(default=0)
    uid2 = models.IntegerField(default=0)
    last_time = models.DateTimeField(auto_now_add=True)    
    def __unicode__(self):
        return str(self.cid)

class MessageManager:
    def addMessage(self,sender,receiver,mcontent):
        chat_list=Chat.objects.filter(Q(uid1=sender)&Q(uid2=receiver)|Q(uid1=receiver)&Q(uid2=sender))
        if chat_list.exists():
            mcid=chat_list[0].cid
        else:
            mcid=self.addChat(sender,receiver)
        m=Message(cid=mcid,sender=sender,content=mcontent)
        m.save()
        chat=chat_list[0]
        chat.last_time=m.send_time
        chat.save()
        


    def addChat(self,muid1,muid2):
        mChat=Chat(uid1=muid1,uid2=muid2)
        mChat.save()
        return mChat.cid
    
    


