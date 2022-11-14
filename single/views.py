from django.http import JsonResponse
from django.shortcuts import render, redirect
from datetime import datetime
from .models import Schedule
import json
from team_project.models import Team

# Create your views here.

def single_day(request):
    schedule = Schedule.objects.all()

    # return HttpResponse(json.dumps(event_arr))
    context = {
        "schedules": schedule
    }

    return render(request, "single/days.html", context)


def single_cal(request):
    all_events = Schedule.objects.all()
    event_arr = []
    for i in all_events:
        event_sub_arr = {}
        event_sub_arr['title'] = i.title
        start_date = datetime.strptime(str(i.date), "%Y-%m-%d").strftime("%Y-%m-%d")
        event_sub_arr['start'] = start_date
        event_arr.append(event_sub_arr)
    data = JsonResponse((event_arr), safe=False)
    datatest = json.dumps(event_arr)
    # return HttpResponse(json.dumps(event_arr))
    print(data, type(data))
    print(datatest, type(datatest))
    # return HttpResponse(json.dumps(event_arr))
    context = {
        "appointment": datatest
    }

    return render(request, "single/calender.html", context)

def single_edit(request):
    posts = Schedule.objects.all()
    teams = Team.objects.all()
    if request.method == 'POST':
        post = Schedule()
        post.title = request.POST.get('title')
        post.startTime = datetime.strptime(request.POST['time1'], '%H:%M').time()
        post.dueTime = datetime.strptime(request.POST.get('time2'), '%H:%M').time()
        if request.POST['team'] == '개인':
            post.how = '개인'
        else:
            post.how = '팀'
            if request.POST['teamSelect']:
                post.team = Team(request.POST['teamSelect'])
        post.save()
        return redirect('post')
    else:
        return render(
            request,
            'single/schedule_form.html',
            {
                'posts': posts,
                'teams': teams
            }
        )

