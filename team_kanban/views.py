from django.shortcuts import render

# Create your views here.
from team_kanban.models import Kanban
from team_project.models import Project


def index(request, pk):
    project = Project.objects.get(pk=pk)#프로젝트의 pk값
    todo = Kanban.objects.filter(team=project, status=0)
    doing = Kanban.objects.filter(team=project, status=1)
    done = Kanban.objects.filter(team=project, status=2)

    return render(
        request,
        'team_kanban/team_kanban.html',
        {
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