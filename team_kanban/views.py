from django.shortcuts import render, redirect, resolve_url

# Create your views here.
from team_kanban import models
from team_kanban.models import Kanban
from team_project.models import Project


def create_kanban(request, p_pk, s_pk):
    post = Project.objects.get(pk=p_pk)
    kanban_status = s_pk
    kanban = models.Kanban()


    if request.method == 'POST':
        kanban.team = post
        kanban.STATUS = kanban_status
        kanban.title = request.POST['title']
        kanban.date_end = request.POST['date_end']
        kanban.introduce = request.POST['introduce']

        kanban.save()
        return redirect(resolve_url('kanban', p_pk))

    return render(
        request,
        'team_kanban/writekanban.html',
    )

def index(request, p_pk):
    project = Project.objects.get(pk=p_pk)#프로젝트의 pk값
    todo = Kanban.objects.filter(team=project, status=0)
    doing = Kanban.objects.filter(team=project, status=1)
    done = Kanban.objects.filter(team=project, status=2)

    return render(
        request,
        'team_kanban/team_kanban.html',
        {
            'post':project,
            'todo':todo,
            'doing':doing,
            'done':done
        }
    )

def detail(request, pk):
    #project = Project.objects.get(pk=pk)  # 프로젝트의 pk값
    #kanban = Kanban.objects.filter(team=project).get(pk=pk)
    kanban = Kanban.objects.get(pk=pk)

    return render(
        request,
        'team_kanban/insidekanban.html',
        {
            'kanban':kanban,
        })