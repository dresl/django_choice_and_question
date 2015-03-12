from django.shortcuts import render
from django.core.wsgi import get_wsgi_application
    from dj_static import Cling

    application = Cling(get_wsgi_application())
# Create your views here.