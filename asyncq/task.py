from celery import task
from member.models import MotssUser
from feed.feedmanager import FeedManager

@task(name="task.add")
def add(x, y):
    return x + y

@task(name="task.insert_user")
def insert_user(username, password, email, ip):
	user = MotssUser.create(username, password, email, ip)
	user.save()
	return user

@task(name="task.thread_feeds")
def thread_feeds(sender_id, thread_id, post_id, ftype, at_users):
	fm = FeedManager()
	return fm.thread_feeds(sender_id, thread_id, post_id, ftype, at_users)
