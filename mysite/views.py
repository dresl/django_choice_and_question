from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import *
from django.views import generic
from django.utils import timezone
from polls.models import Choice, Question

def home(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('home.html')
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
    })
    return HttpResponse(template.render(context))