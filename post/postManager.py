from django.db import transaction
from cgi import escape
from member.models import MotssUser
from post.models import Thread, Post, Test, Attachment, TagThread
from post.xssparser import XssParser

class PostManager:
	@transaction.commit_on_success
	def create_thread(self, author, subject, message, readperm=1, attaches=[], tags=None):
		subject = escape(subject)
		xss = XssParser()
		xss.feed(message)
		message = xss.result
		hasAttach = (len(attaches)>0)
		post = Post(author=author, authorip=author.loginip, \
			subject=subject, message=message, position=0, hasattach=hasAttach, \
			readperm=readperm)
		thread = Thread(author=author, subject=subject, abstract=post.getAbstract(), \
			hasattach=hasAttach, tags=tags)
		thread.save()
		post.thread = thread
		post.save()
		taglist = []
		if tags != None:
			for tag in tags:
				tag = escape(tag)
				taglist.append(TagThread(tagname=tag, tid=thread.tid, lastposttime=thread.lastposttime, \
					heats=thread.heats))
			TagThread.objects.bulk_create(taglist)
		return thread

	@transaction.commit_on_success
	def reply_thread(self, author, tid, subject, message, readperm=1, attaches=[]):
		subject = escape(subject)
		xss = XssParser()
		xss.feed(message)
		message = xss.result
		hasAttach = (len(attaches)>0)
		qt = Thread.objects.filter(tid=tid)
		if not qt.exists():
			return None
		thread = qt.get()
		position = thread.maxposition
		thread.replied_by(author)
		post = Post(thread=thread, author=author, authorip=author.loginip, subject=subject, \
			message=message, position=position, hasattach=hasAttach, readperm=readperm)
		post.save()
		return  post

	def get_thread_posts(self, tid, start, count) :
		posts = Post.objects.filter(thread_id=tid).order_by('position')[start:start+count].select_related()
		return posts

#	def get_subscribed_threads(self, author, start, count) :
#		tags = author.subscribed_tags()
#		tid_qs = TagThread.objects.filter(tagname__in=tags).order_by('-heats', '-lastposttime').\
#			values('tid').distinct()[start:start+count]
#		tids = []
#		for item in tid_qs:
#			tids.append(item['tid'])
#		threads = Thread.objects.filter(tid__in=tids).order_by('-heats', '-lastposttime').select_related()
#		return threads

