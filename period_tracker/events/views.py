from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe

from .models import *
from .utils import Calendar


def events(request):
    template = loader.get_template('clock.html')
    return HttpResponse(template.render())

def calender(request):
    template = loader.get_template('calender.html')
    return HttpResponse(template.render())

def index(request):
    return HttpResponse('hello')

class CalendarView(generic.ListView):
    model = Events
    template_name = 'events/'
