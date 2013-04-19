from django.conf.urls import patterns, include, url

from django.contrib import admin
from motss import views
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^index/Images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'C:/Users/Ghost/Documents/GitHub/motss/member/templates/index/Images'}), 
    url(r'^index/',views.index),
    
    url(r'^member/', include('member.urls', namespace="member")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^message/', include('short_message.urls', namespace="short_message")),
)
