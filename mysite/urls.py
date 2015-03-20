from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^hovno/', include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
)