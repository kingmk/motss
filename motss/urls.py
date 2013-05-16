from django.conf.urls import patterns, include, url

from django.contrib import admin
from motss import views
from motss import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^home/', views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^member/', include('member.urls', namespace="member")),
    url(r'^post/', include('post.urls', namespace="post")),
    url(r'^message/', include('short_message.urls', namespace="short_message")),
    url(r'^test/',views.test,name='test'),
    url(r'^static/(?P<path>.*)$','django.views.static.serve', {'document_root': settings.STATICFILES_DIRS[0]}),
)
