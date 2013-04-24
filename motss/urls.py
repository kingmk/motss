from django.conf.urls import patterns, include, url

from django.contrib import admin
from motss import views
from motss import settings


admin.autodiscover()

urlpatterns = patterns('',    
    url(r'^index/',include('index.urls', namespace="index")),
    url(r'^member/', include('member.urls', namespace="member")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^message/', include('short_message.urls', namespace="short_message")),
    url(r'^test/',views.test,name='test'),
    url(r'^static/(?P<path>.*)$','django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
