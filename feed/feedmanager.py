from django.db import transaction
from feed.models import Feed
from post.models import Thread, Post
from member.models import MotssUser, MotssFollow

class FeedManager(object):
	
	def send_feed(self, sender_id, thread_id, post_id, ftype):
		follows = MotssFollow.objects.filter(follow_id=sender_id)
		follower_ids = []
		for follow in follows:
			follower_ids.append(follow.user_id)

		update_feeds_id = []
		insert_feeds = []

		# find the existing feeds related with the thread owned by the followers
		exist_feeds = Feed.objects.filter(thread_id=thread_id, ishistory=False, \
			recvid__in=follower_ids)
		for exist_item in exist_feeds:
			update_feeds_id.append(exist_item.fid)

		# update all the found feeds to history feeds
		Feed.objects.filter(fid__in=update_feeds_id).update(ishistory=True)

		# insert all feeds to the followers' feeds list
		for follower_id in follower_ids:
			feed = Feed(recvid=follower_id, sendid=sender_id, thread_id=thread_id, \
				post_id=post_id, ftype=ftype)
			insert_feeds.append(feed)
		Feed.objects.bulk_create(insert_feeds)
