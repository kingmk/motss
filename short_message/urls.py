from django.conf.urls import patterns, url

from short_message import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
