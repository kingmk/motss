from celery import task
from member.models import MotssUser

@task(name="task.add")
def add(x, y):
    return x + y

@task(name="task.insert_user")
def insert_user(username, password, email, ip):
	user = MotssUser.create(username, password, email, ip)
	user.save()
	return user