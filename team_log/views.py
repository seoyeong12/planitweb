from django.shortcuts import render, redirect, resolve_url
from django.views.generic import CreateView

from . import models
from .models import Log
from team_project.models import Project

# Create your views here.


def index(request, p_pk):
    post = Project.objects.get(pk=p_pk)
    logs = Log.objects.filter(team=post.team)
    log = models.Log()

    if request.method == 'POST' and 'sub_btn' in request.POST:
        log.team = post.team
        log.status = False
        log.title = request.POST['input']

        log.save()
        return redirect(resolve_url('log', p_pk))


    return render(
        request,
        'team_log/backlog.html',
        {
            'post':post,
            'logs': logs,
        })

def update_log(request, p_pk, l_pk):
    post = Project.objects.get(pk=p_pk)
    logs = Log.objects.filter(team=post.team)
    log = Log.objects.get(team=post.team, pk=l_pk)

    if request.method == 'POST' and 'check_btn' in request.POST:
        if request.POST['check_btn'] == "True":
            log.status = False
            log.save()
            return redirect(resolve_url('log', p_pk))
        elif request.POST['check_btn'] == "False":
            log.status = True
            log.save()
            return redirect(resolve_url('log', p_pk))

    if request.method == 'POST' and 'delete' in request.POST:
        log.delete()
        return redirect(resolve_url('log', p_pk))

    return render(request,
                  'team_log/backlog.html',
                  {
                      'post':post,
                      'logs':logs,
                  })

