from django.db import models
from post.models import Thread, Post

class Feed(models.Model) :
	FTYPE_OTHER = 0
	FTYPE_CREATE = 1
	FTYPE_REPLY = 2
	FTYPE_AT = 3
	FTYPE_CHOICES = (
		(FTYPE_CREATE, 'create thread'),
		(FTYPE_REPLY, 'reply thread'),
		(FTYPE_AT, 'at in thread'),
	)
	fid = models.AutoField(primary_key=True)
	recvid = models.IntegerField(db_index=True)
	sendid = models.IntegerField(db_index=True)
	thread = models.ForeignKey(Thread, related_name='feed', db_index=True)
	post = models.ForeignKey(Post, related_name='feed', db_index=True)
	createtime = models.DateTimeField(auto_now_add=True, db_index=True)
	ftype = models.SmallIntegerField(choices=FTYPE_CHOICES, default=FTYPE_OTHER, db_index=True)
	ishistory = models.BooleanField(default=False, db_index=True)