from django.shortcuts import render
from .models import Schedule
from django.views.generic import CreateView
# Create your views here.

def single_day(request):
    schedules = Schedule.objects.all().order_by('date', 'startTime')
    return render(
        request,
        'single/days.html',
        {
            'schedules' : schedules
        }
    )

def single_cal(request):
    return render(
        request,
        'single/calender.html',
    )

def single_edit(request):
    return render(
        request,
        'single/edit.html',
    )