import datetime
from django.utils import timezone
from django.db import models
from member.models import Member


class Thread(models.Model):
    tid = models.AutoField(primary_key=True)
    reftid = models.BigIntegerField(default=-1, null=True, blank=True)
    typeid = models.SmallIntegerField(default=0, db_index=True, blank=True)
    authorname = models.CharField(max_length=15)
    authorid = models.BigIntegerField(db_index=True)
    pubtime = models.DateTimeField(auto_now_add=True, db_index=True, blank=True)
    maxposition = models.IntegerField(default=1, blank=True)
    lastposter = models.CharField(max_length=15, null=True, blank=True)
    lastposterid = models.BigIntegerField(default=-1, null=True, blank=True)
    lastposttime = models.DateTimeField(auto_now=True, db_index=True, blank=True)
    subject = models.CharField(max_length=400)
    abstract = models.CharField(max_length=400, null=True, blank=True)
    views = models.BigIntegerField(default=0, blank=True)
    replies = models.IntegerField(default=0, blank=True)
    status = models.SmallIntegerField(default=0, db_index=True, blank=True)
    hasattach = models.BooleanField(db_index=True, default=0, blank=True)
    heats = models.BigIntegerField(db_index=True, default=100, blank=True)
    tags = models.CharField(max_length=500, null=True, blank=True)

    def repliedBy(self, author):
        self.maxposition += 1
        self.lastposter = author.username
        self.lastposterid = author.uid
        self.replies += 1
        self.heats = 100
        return

    def __unicode__(self):
    	s = 'tid:'+str(self.tid)
    	s += ', reftid:'+str(self.reftid)
    	s += ', authorname:'+str(self.authorname)
    	s += ', authorid:'+str(self.authorid)
    	s += ', pubtime:'+str(self.pubtime)
    	s += ', maxposition:'+str(self.maxposition)
    	s += ', lastposter:'+str(self.lastposter)
    	s += ', lastposterid:'+str(self.lastposterid)
    	s += ', lastpostertime:'+str(self.lastposttime)
    	s += ', subject:'+str(self.subject)
    	s += ', abstract:'+str(self.abstract)
    	s += ', views:'+str(self.views)
    	s += ', replies:'+str(self.replies)
    	s += ', status:'+str(self.status)
    	s += ', hasattach:'+str(self.hasattach)
    	s += ', heats:'+str(self.heats)
    	s += ', tags:'+str(self.tags)
    	return s

class Post(models.Model):
    pid = models.AutoField(primary_key=True)
    tid = models.BigIntegerField(db_index=True)
    authorname = models.CharField(max_length=15)
    authorid = models.BigIntegerField(db_index=True)
    authorip = models.CharField(max_length=100, null=True)
    pubtime = models.DateTimeField(auto_now_add=True, db_index=True, blank=True)
    subject = models.CharField(max_length=400, null=True)
    message = models.TextField(null=True)
    hasattach = models.BooleanField(db_index=True, default=0, blank=True)
    invisible = models.BooleanField(db_index=True, default=0, blank=True)
    status = models.SmallIntegerField(default=0, db_index=True, blank=True)
    position = models.IntegerField(db_index=True)
    readperm = models.IntegerField(default=1, blank=True)
    attaches = models.TextField(null=True, blank=True)

    def __unicode__(self):
    	s = 'pid:'+str(self.pid)
    	s += 'tid:'+str(self.tid)
    	s += ', authorname:'+str(self.authorname)
    	s += ', authorid:'+str(self.authorid)
    	s += ', authorip:'+str(self.authorip)
    	s += ', pubtime:'+str(self.pubtime)
    	s += ', subject:'+str(self.subject)
    	s += ', message:'+str(self.message)
    	s += ', hasattach:'+str(self.hasattach)
    	s += ', invisible:'+str(self.invisible)
    	s += ', status:'+str(self.status)
    	s += ', position:'+str(self.position)
    	s += ', readperm:'+str(self.readperm)
    	s += ', attaches:'+str(self.attaches)
    	return s

    def getAbstract(self):
    	return self.message

class Attachment(models.Model):
	ATT_OTHER = 0
	ATT_IMAGE = 1
	ATT_AUDIO = 2
	ATT_VIDEO = 3
	ATT_PACKAGE = 4
	ATTACH_CHOICES = (
		(ATT_OTHER, 'other'),
		(ATT_IMAGE, 'image'),
		(ATT_AUDIO, 'audio'),
		(ATT_VIDEO, 'video'),
		(ATT_PACKAGE, 'package'),
	)

	aid = models.AutoField(primary_key=True)
	uid = models.BigIntegerField(db_index=True)
	uploadtime = models.DateTimeField(auto_now_add=True, db_index=True, blank=True)
	url = models.CharField(max_length=1024)
	filename = models.CharField(max_length=1024, default='unknown', blank=True)
	filesize = models.IntegerField(default=0, blank=True)
	filetype = models.SmallIntegerField(choices=ATTACH_CHOICES,default=ATT_OTHER)
	width = models.IntegerField(null=True, default=0, blank=True)
	height = models.IntegerField(null=True, default=0, blank=True)
	thumbid = models.BigIntegerField(null=True, blank=True)
	duration = models.IntegerField(null=True, default=0, blank=True)
	extend = models.TextField(null=True, blank=True)

	def __unicode__(self):
		s = 'aid:'+str(self.aid)
		s += ', uid:'+str(self.uid)
		s += ', uploadtime:'+str(self.uploadtime)
		s += ', filename:'+str(self.filename)
		s += ', filesize:'+str(self.filesize)
		s += ', filetype:'+str(self.filetype)
		s += ', width:'+str(self.width)
		s += ', height:'+str(self.height)
		s += ', thumbid:'+str(self.thumbid)
		s += ', duration:'+str(self.duration)
		s += ', extend:'+str(self.extend)
		return s

class TagThread(models.Model):
	tagname = models.CharField(max_length=50, db_index=True)
	tid = models.BigIntegerField(db_index=True)
	lastposttime = models.DateTimeField(auto_now=True, db_index=True, blank=True)
	heats = models.BigIntegerField(db_index=True, default=100, blank=True)

	def __unicode__(self):
		s = 'tagname:'+str(self.tagname)
		s += ', tid:'+str(self.tid)
		s += ', lastposttime:'+str(self.lastposttime)
		s += ', heats:'+str(self.heats)
		return s

class Test(models.Model):
	author = models.ForeignKey(Member)
	prop = models.CharField(max_length=100)

 	def __unicode__(self):
 		return str(self.author) + ', prop:'+str(self.prop)

 	def testAny(self, obj):
 		for ele in obj:
 			print ele
 		return
