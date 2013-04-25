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
2. Add the following lines to settings.py:<br/>
import djcelery<br/>
djcelery.setup_loader()
3. Create the celery database tables: <br/>
python manage.py syncdb
4. Use RabbitMQ as the broker (installation guide: http://www.rabbitmq.com/download.html)<br/>
start the server:<br/>
$ sudo rabbitmq-server -detached<br/>
check the status:<br/>
$ sudo rabbitmqctl status<br/>
stop the server:<br/>
$ sudo rabbitmqctl stop
5. Add BROKER_URL into settings.py:<br/>
BROKER_URL = 'amqp://guest:guest@localhost:5672/'
6. Start the worker process:<br/>
$ python manage.py celery worker --loglevel=info
7. Add such lines into settings.py:<br/>
CELERY_RESULT_BACKEND = "amqp"<br/>
CELERY_IMPORTS = ("app.module", )<br/>
INSTALLED_APPS = (<br/>
    ...,<br/>
    'djcelery',<br/>
    'app',<br/>
)<br/>
where app is the name of app used in project, module is the name of module




