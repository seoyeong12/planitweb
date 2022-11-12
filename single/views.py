from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
import json

from django.urls import reverse
from datetime import datetime
from .models import Schedule
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
    posts = Schedule.objects.all()

    return render(request, 'single/calender.html',
                  {
                      'posts' : posts
                  })



def single_edit(request):
    if request.method == 'POST':
        post = Schedule()
        post.title = request.POST.get('title')
        post.startTime = datetime.strptime(request.POST['time1'], '%H:%M').time()
        post.dueTime = datetime.strptime(request.POST.get('time2'), '%H:%M').time()
        post.save()
        return redirect('post')
    else:
        return render(
            request,
            'single/schedule_form.html',
        )