from django.conf.urls import patterns, url

from post import views

urlpatterns = patterns('',
    url(r'^createthread/', views.create_thread, name='createthread'),
)