from django.urls import path, include
from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('events/', views.events, name='events'),
    path('events/calender', views.calender, name='calendar')
]
