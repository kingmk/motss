from member.models import Member
from post.models import Thread
from post.models import Post
from post.models import Attachment
from post.models import TagThread

class PostManager:
	def createNewThread(self, author, subject, message, readperm=1, attaches=None, tags=None):
		hasAttach = (attaches!=None)
		post = Post(authorname=author.username, authorid=author.uid, authorip=author.loginip, \
			subject=subject, message=message, position=0, hasattach=hasAttach, \
			attaches=attaches, readperm=readperm)
		thread = Thread(authorname=author.username, authorid=author.uid, subject=subject, \
			abstract=post.getAbstract(), hasattach=hasAttach, tags=tags)
		thread.save()
		post.tid = thread.tid
		post.save()
		if tags != None:
			for tag in tags:
				tagT = TagThread(tagname=tag, tid=thread.tid, lastposttime=thread.lastposttime, \
					heats=thread.heats)
				tagT.save()
		return thread

	def replyThread(self, author, tid, subject, message, readperm=1, attaches=None):
		hasAttach = (attaches!=None)
		try:
			thread = Thread.objects.get(tid=tid)
			thread.repliedBy(author)
			post = Post(tid=tid, authorname=author.username, authorid=author.uid, authorip=author.loginip, \
				subject=subject, message=message, position=thread.maxposition, hasattach=hasAttach, \
				attaches=attaches, readperm=readperm)
			thread.save()
			post.save()
		except Thread.DoesNotExist:
			return None
		except:
			return None
		return  post