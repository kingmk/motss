from django.db import models
from post.models import Thread, Post

class Feed(models.Model) :
	FTYPE_OTHER = 0
	FTYPE_CREATE = 1
	FTYPE_REPLY = 2
	FTYPE_CHOICES = (
		(FTYPE_OTHER, 'other'),
		(FTYPE_CREATE, 'create thread'),
		(FTYPE_REPLY, 'reply thread'),
	)
	fid = models.AutoField(primary_key=True)
	recvid = models.IntegerField(db_index=True)
	sendid = models.IntegerField(db_index=True)
	thread = models.ForeignKey(Thread, related_name='feed', db_index=True)
	post = models.ForeignKey(Post, related_name='feed', db_index=True)
	createtime = models.DateTimeField(auto_now_add=True, db_index=True)
	feed_at = models.BooleanField(db_index=0, default=False)
	ftype = models.SmallIntegerField(choices=FTYPE_CHOICES, default=FTYPE_OTHER, db_index=True)
	ishistory = models.BooleanField(default=False, db_index=True)

	def __unicode__(self):
		s = 'id:%s, recvid:%s, sendid:%s, thread_id:%s, post_id:%s, createtime:%s, at:%s, type:%s, history:%s'\
			%(str(self.fid), str(self.recvid), str(self.sendid), str(self.thread_id), \
			str(self.post_id), str(self.createtime), str(self.feed_at), str(self.ftype),\
			str(self.ishistory))
		return s
