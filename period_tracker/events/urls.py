from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.events, name='events'),
    path('events/calender', views.calender, name='calendar')
]