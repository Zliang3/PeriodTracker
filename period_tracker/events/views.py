from django.http import HttpResponse
from django.template import loader


def events(request):
    template = loader.get_template('clock.html')
    return HttpResponse(template.render())


def calender(request):
    template = loader.get_template('calender.html')
    return HttpResponse(template.render())
