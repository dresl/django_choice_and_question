from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import *

urlpatterns = patterns('',
	url(r'^$', hello.views.index, name='index'),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
)
