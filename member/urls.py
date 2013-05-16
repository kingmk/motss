from django.conf.urls import patterns, url

from member import views

urlpatterns = patterns('',
    url(r'^login/', views.viewlogin, name='viewlogin'),
    url(r'^dologin/', views.dologin, name='dologin'),
    url(r'^dologout/', views.dologout, name='dologout'),
)