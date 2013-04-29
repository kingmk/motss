from django.db import transaction
from datetime import datetime
from feed.models import Feed
from post.models import Thread, Post
from member.models import MotssUser, MotssFollow
from member.exceptions import UserException, DuplicateException, \
	RegisterException, NoUserLoginException, WrongPasswordException,\
	NoSuchUserException, FollowedException, FollowDeniedException,\
	FollowSelfException

class FeedManager(object):
	
	def thread_feeds(self, sender_id, thread_id, post_id, ftype, at_users=[]):
		follows = MotssFollow.objects.filter(follow_id=sender_id)
		follower_ids = []
		for follow in follows:
			follower_ids.append(follow.user_id)

		update_feeds_id = []
		insert_feeds = []
		at_ids = []
		for user in at_users:
			at_ids.append(user['id'])

		# find the existing feeds related with the thread owned by the followers
		exist_feeds = Feed.objects.filter(thread_id=thread_id, ishistory=False, \
			recvid__in=follower_ids)
		for exist_item in exist_feeds:
			update_feeds_id.append(exist_item.fid)

		# update all the found feeds to history feeds
		Feed.objects.filter(fid__in=update_feeds_id).update(ishistory=True)

		# insert all feeds to the followers' feeds list
		for follower_id in follower_ids:
			f_at = False
			if follower_id in at_ids:
				f_at = True
				at_ids.remove(follower_id)
			feed = Feed(recvid=follower_id, sendid=sender_id, thread_id=thread_id, \
				post_id=post_id, ftype=ftype, feed_at=f_at)
			insert_feeds.append(feed)

		print at_ids
		for at_id in at_ids:
			feed = Feed(recvid=at_id, sendid=sender_id, thread_id=thread_id, \
				post_id=post_id, ftype=ftype, feed_at=True)
			insert_feeds.append(feed)

		Feed.objects.bulk_create(insert_feeds)

		return follower_ids

	def get_feeds(self, recvid, ftype_list, before_time=None, count=20) :
		qt = MotssUser.objects.filter(id=recvid)
		if not qt.exists():
			raise NoSuchUserException()
		if before_time is None:
			before_time = datetime.now()

		feeds = Feed.objects.filter(recvid=recvid, ishistory=False, \
			ftype__in=ftype_list, createtime__lt=before_time).\
			order_by('-createtime').select_related()[0:count]
		return feeds



