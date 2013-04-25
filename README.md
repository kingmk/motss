motss
=====

www.motss.info forum's source code


Apps included:

* member
* post
* short_message


Depends: Django-Celery
refer: http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html

1. pip install django-celery
2. Add the following lines to settings.py:
	import djcelery
	djcelery.setup_loader()
3. Create the celery database tables: python manage.py syncdb
4. Use RabbitMQ as the broker (installation guide: http://www.rabbitmq.com/download.html)
	start the server:
	$ sudo rabbitmq-server -detached
	check the status:
	$ sudo rabbitmqctl status
	stop the server:
	$ sudo rabbitmqctl stop
5. Add BROKER_URL into settings.py:
	BROKER_URL = 'amqp://guest:guest@localhost:5672/'
6. Start the worker process:
	$ python manage.py celery worker --loglevel=info
7. Add such lines into settings.py:
	CELERY_RESULT_BACKEND = "amqp"
	CELERY_IMPORTS = ("app.module", )
	INSTALLED_APPS = (
    	...,
    	'djcelery',
    	'app',
	)
	where app is the name of app used in project, module is the name of module




