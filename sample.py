from member.models import MotssUser
from post.models import Thread, Post, Test, Attachment, TagThread
from post.postmanager import PostManager


class Sample:

	@classmethod
	def insert_member(cls):
		ip = '127.0.0.1'
		user1 = MotssUser.create('test002', '123456', 'test002@163.com', ip)
		user2 = MotssUser.create('test003', '123456', 'test003@163.com', ip)
		print user1
		print user2
		MotssUser.objects.bulk_create([user1, user2])

	@classmethod
	def insert_thread(cls):
		author = MotssUser.objects.all()[1]
		thread = Thread(author=author, subject='test insert thread')
		thread.save()
		return thread

	@classmethod
	def insert_post(cls):
		author = MotssUser.objects.all()[1]
		thread = Thread.objects.all()[0]
		post = Post(thread=thread, author=author, authorip='127.0.0.1', \
			message='test insert post', position=thread.maxposition)
		post.save()
		return post

	@classmethod
	def pm_create_thread(cls):
		author = MotssUser.objects.all()[1]
		pm = PostManager()
		thread = pm.create_thread(author,'test process of creating thread', 'test process of creating thread message', 1, [], ['tag2', 'tag3'])
		return thread

	@classmethod
	def pm_reply_thread(cls):
		author = MotssUser.objects.all()[1]
		thread = Thread.objects.all()[1]
		pm = PostManager()
		post = pm.reply_thread(author, thread.tid, 'test process of replying thread', \
			'test process of replying thread message')
		return post

	@classmethod
	def pm_get_thread_posts(cls):
		thread = Thread.objects.all()[0]
		pm = PostManager()
		posts = pm.get_thread_posts(thread.tid, 0, 20)
		return posts

#	@classmethod
#	def pm_subscriebed_threads(cls):
#		author = MotssUser.objects.all()[1]
#		pm = PostManager()
#		threads = pm.get_subscribed_threads(author, 0, 20)
#		return threads