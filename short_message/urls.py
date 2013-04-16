from django.conf.urls import patterns, url

from short_message import views

urlpatterns = patterns('',
    url(r'^chat/(\d)', views.chat),                   
    url(r'^', views.index),   
)
