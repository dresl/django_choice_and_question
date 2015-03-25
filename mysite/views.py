from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import *
from django.views import generic
from django.utils import timezone
from polls.models import Choice, Question

def index(request):
    return HttpResponse("THIS IS INDEX PAGE")