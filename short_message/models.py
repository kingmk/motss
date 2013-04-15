import datetime
from django.utils import timezone
from django.db import models

class Message (models.Model):
    mid = models.AutoField(primary_key=True)
    cid = models.SmallIntegerField(default=0)  
    content = models.CharField(max_length=300)
    send_time = models.DateTimeField(auto_now_add=True)    

    def _unicode_(self):
        return self.mid+self.content

class Chat (models.Model):
    cid = models.AutoField(primary_key=True)  
    sender = models.IntegerField(default=0)
    receiver = models.IntegerField(default=0)
    last_time = models.DateTimeField(auto_now_add=True)

    def _unicode_(self):
        return self.cid+self.sender+self.receiver
    
    


