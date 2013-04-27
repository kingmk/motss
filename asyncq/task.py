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

@task(name="task.send_feeds")
def send_feeds(sender_id, thread_id, post_id, ftype):
	fm = FeedManager()
	return fm.send_feeds(sender_id, thread_id, post_id, ftype)
