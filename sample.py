from member.models import MotssUser, MotssProfile, MotssFollow
from member.membermanager import MemberManager
from post.models import Thread, Post, Test, Attachment, TagThread
from post.postmanager import PostManager
from feed.models import Feed
from feed.feedmanager import FeedManager

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
		thread = pm.create_thread(author,'test feeds sending with at',\
		 'test feeds sending @yuxinjin @nonexist @test002', 1, [], ['tag1', 'tag4'])
		return thread

	@classmethod
	def pm_reply_thread(cls):
		author = MotssUser.objects.all()[1]
		thread = Thread.objects.all()[2]
		pm = PostManager()
		post = pm.reply_thread(author, thread.tid, 'test feeds sending', \
			'test feeds sending @yuxinjin @nonexist @test002')
		return post

	@classmethod
	def pm_get_thread_posts(cls):
		thread = Thread.objects.all()[0]
		pm = PostManager()
		posts = pm.get_thread_posts(thread.tid, 0, 20)
		return posts

	@classmethod
	def mm_follow(cls):
		users = MotssUser.objects.all()
		user1 = users[0]
		user2 = users[3]
		mm = MemberManager()
		follow_relation = mm.follow(user1, user2.id)
		return follow_relation

	@classmethod
	def mm_get_user_follows(cls):
		user = MotssUser.objects.all()[0]
		mm = MemberManager()
		follows = mm.get_user_follows(user, 0, 10)
		return follows

	@classmethod
	def fm_get_feeds(cls):
		fm = FeedManager()
		posts = Post.objects.all().order_by('-pubtime')
		timestamp = posts[0].pubtime
		type_list = [0, 1, 2, 3]
		feeds = fm.get_feeds(6, type_list)
		print feeds

		feeds = fm.get_feeds(6, type_list, timestamp)
		print feeds

#	@classmethod
#	def pm_subscriebed_threads(cls):
#		author = MotssUser.objects.all()[1]
#		pm = PostManager()
#		threads = pm.get_subscribed_threads(author, 0, 20)
#		return threads
	@classmethod
	def exception_user(cls):
		from member.exceptions import UserException, DuplicateException, \
		RegisterException, NoUserLoginException, WrongPasswordException,\
		NoSuchUserException, FollowedException, FollowDeniedException

		base_e = NotImplementedError('base error')
		try:
			raise UserException(cause=base_e)
		except UserException, e:
			print e
			print e.msg

		try:
			raise DuplicateException(cause=base_e, username='testuser')
		except DuplicateException, e:
			print e
			print e.msg

		try:
			raise RegisterException(cause=base_e, note='Password wrong')
		except RegisterException, e:
			print e
			print e.msg

		try:
			raise NoUserLoginException(cause=base_e, username='testuser')
		except NoUserLoginException, e:
			print e
			print e.msg

		try:
			raise WrongPasswordException(cause=base_e)
		except WrongPasswordException, e:
			print e
			print e.msg

		try:
			raise NoSuchUserException(cause=base_e, username='testuser')
		except NoSuchUserException, e:
			print e
			print e.msg

		try:
			raise FollowedException(cause=base_e, username='testuser')
		except FollowedException, e:
			print e
			print e.msg
			
		try:
			raise FollowDeniedException(cause=base_e, username='testuser')
		except FollowDeniedException, e:
			print e
			print e.msg

	@classmethod
	def exception_post(cls):
		from post.exceptions import PostException, IllegalContentException, \
		NoSuchThreadException, ThreadDeletedException, ThreadClosedException, \
		AttachOverSizedException, AttachUnsupportException

		base_e = NotImplementedError('base error')
		try:
			raise PostException(cause=base_e)
		except PostException, e:
			print e
			print e.msg

		try:
			raise IllegalContentException(cause=base_e, malcontent='test')
		except PostException, e:
			print e
			print e.msg

		try:
			raise NoSuchThreadException(cause=base_e, tid=111)
		except PostException, e:
			print e
			print e.msg

		try:
			raise ThreadDeletedException(cause=base_e, tid=111)
		except PostException, e:
			print e
			print e.msg
		try:
			raise ThreadClosedException(cause=base_e, tid=111)
		except PostException, e:
			print e
			print e.msg

		try:
			raise AttachOverSizedException(cause=base_e, size=199982)
		except PostException, e:
			print e
			print e.msg

		try:
			raise AttachUnsupportException(cause=base_e, attach_type='mmp')
		except PostException, e:
			print e
			print e.msg