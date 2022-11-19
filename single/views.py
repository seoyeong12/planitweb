from datetime import datetime

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Schedule
import json
from team_project.models import Team

# Create your views here.

def single_day(request):
    schedule = Schedule.objects.all()
    teams = Team.objects.all()
    event_arr = []
    for i in schedule:
        event_sub_arr = {}
        event_sub_arr['title'] = i.title
        start_date = datetime.strptime(str(i.date), "%Y-%m-%d").strftime("%Y-%m-%d")
        start_time = datetime.strptime(str(i.startTime), "%H:%M:%S").strftime("%H:%M:%S")
        res1 = start_date + "T" + start_time
        event_sub_arr['start'] = res1
        end_time = datetime.strptime(str(i.dueTime), "%H:%M:%S").strftime("%H:%M:%S")
        res2 = start_date + "T" + end_time
        event_sub_arr['end'] = res2
        event_arr.append(event_sub_arr)
    data = JsonResponse((event_arr), safe=False)
    datatest = json.dumps(event_arr)
    # return HttpResponse(json.dumps(event_arr))
    print(data, type(data))
    print(datatest, type(datatest))
    # return HttpResponse(json.dumps(event_arr))
    context = {
        "schedule": schedule,
        "appointment": datatest,
        "teams": teams,
    }

    return render(request, "single/days.html", context)


def single_cal(request):
    all_events = Schedule.objects.all()
    event_arr = []
    for i in all_events:
        event_sub_arr = {}
        event_sub_arr['title'] = i.title
        start_date = datetime.strptime(str(i.date), "%Y-%m-%d").strftime("%Y-%m-%d")
        start_time = datetime.strptime(str(i.startTime), "%H:%M:%S").strftime("%H:%M:%S")
        res = start_date+"T"+start_time
        event_sub_arr['start'] = res
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
        post.date = datetime.strptime(request.POST.get('date'), '%Y-%m-%d')
        if request.POST['team'] == '개인':
            post.how = '개인'
        else:
            post.how = '팀'
            if request.POST['teamSelect']:
                post.team = Team(request.POST['teamSelect'])
        post.save()
        return redirect('single')
    else:
        return render(
            request,
            'single/schedule_form.html',
            {
                'posts': posts,
                'teams': teams
            }
        )
def single_modify(request, pk):
    posts = Schedule.objects.get(pk=pk)
    allteam = Team.objects.all()

    if request.method == 'POST':
        posts.title = request.POST['title']
        posts.startTime = datetime.strptime(request.POST['time1'], '%H:%M').time()
        posts.dueTime = datetime.strptime(request.POST['time2'], '%H:%M').time()
        posts.date = datetime.strptime(request.POST['date'], '%Y-%m-%d')
        if request.POST['team'] == '개인':
            posts.team = None
            posts.how = '개인'
        else:
            posts.how = '팀'
            if request.POST['teamSelect']:
                posts.team = Team(request.POST.get('teamSelect'))
        posts.save()
        return redirect('single')
    else:
        return render(
            request,
            'single/modify_post.html',
            {
                'posts_modi': posts,
                'allteam': allteam,
            }
        )


def single_delete(request, pk):
    posts = Schedule.objects.get(pk=pk)
    posts.delete()
    return redirect('single')