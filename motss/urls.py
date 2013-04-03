from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^member/', include('member.urls', namespace="member")),
	url(r'^admin/', include(admin.site.urls)),
)
