from django.conf.urls import *
from django.contrib import *
from django.http import *

import polls.views

urlpatterns = patterns('',
	url(r'^$', mysite.views.index, name='index'),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
)
