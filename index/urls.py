from django.conf.urls import patterns, include, url

from index import views

urlpatterns = patterns('',    
    url(r'^Images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'C:/Users/Ghost/Documents/GitHub/motss/index/templates/index/Images'}),
    url(r'check/',views.check,name='check'),
    url(r'^',views.index),
    
)
 
