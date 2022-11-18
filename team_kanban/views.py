from django.shortcuts import render, redirect, resolve_url

# Create your views here.
from team_kanban import models
from team_kanban.models import Kanban
from team_project.models import Project, Participant


#칸반 생성
#http://127.0.0.1:8000/team/프로젝트pk값/kanban/프로젝트 상태 pk값/create_kanban
def create_kanban(request, p_pk, s_pk):
    post = Project.objects.get(pk=p_pk)
    kanban_status = s_pk #기존 status
    kanban = models.Kanban()

    participants = Participant.objects.filter(team=post.team)

    if request.method == 'POST':
        kanban.team = post.team
        if (request.POST['status'] == 'todo'):
            kanban.status = 0
        elif (request.POST['status'] == 'doing'):
            kanban.status = 1
        else:
            kanban.status = 2
        kanban.title = request.POST['title']
        kanban.date_end = request.POST['date_end']
        kanban.introduce = request.POST['introduce']

        kanban.save()
        #저장 후 창 닫고 상위 페이지가 새로고침 되어야함
        return redirect(resolve_url('kanban', p_pk))

    return render(
        request,
        'team_kanban/writekanban.html',
        {
            'status':kanban_status,
            'participants': participants,
        }
    )

#기존의 칸반 보여줌
#http://127.0.0.1:8000/team/프로젝트pk/kanban/
def index(request, p_pk):
    project = Project.objects.get(pk=p_pk)#프로젝트의 pk값
    todo = Kanban.objects.filter(team=project.team, status=0)
    doing = Kanban.objects.filter(team=project.team, status=1)
    done = Kanban.objects.filter(team=project.team, status=2)

    participants = Participant.objects.filter(team=project.team)

    return render(
        request,
        'team_kanban/kanban.html',
        {
            'post':project,
            'todo':todo,
            'doing':doing,
            'done':done,
            'participants':participants,

        }
    )

#칸반 상세 페이지
#http://127.0.0.1:8000/team/프로젝트 pk값/kanban/프로젝트의 상태 pk값/데이터베이스pk값/
def detail(request, p_pk, s_pk, i_pk):
    project = Project.objects.get(pk=p_pk)  # 프로젝트의 pk값
    kanban = Kanban.objects.get(team=project.team, pk=i_pk)
    todo = Kanban.objects.filter(team=project.team, status=s_pk).get(pk=i_pk)
    doing = Kanban.objects.filter(team=project.team, status=s_pk).get(pk=i_pk)
    done = Kanban.objects.filter(team=project.team, status=s_pk).get(pk=i_pk)

    participants = Participant.objects.filter(team=project.team)

    return render(
        request,
        'team_kanban/insidekanban.html',
        {
            'post':project,
            'kanban':kanban,
            'todo': todo,
            'doing': doing,
            'done': done,
            'participants': participants,
        }
        )

def rewrite_kanban(request, p_pk, s_pk, i_pk):
    project = Project.objects.get(pk=p_pk)  # 프로젝트의 pk값
    kanban = Kanban.objects.get(team=project.team, pk=i_pk)

    participants = Participant.objects.filter(team=project.team)

    #변경된 경우
    if request.method == 'POST':
        kanban.team = project.team  #고정
        kanban.title = request.POST['title']
        if(request.POST['status'] == 'todo'):
            kanban.status = 0
        elif(request.POST['status'] == 'doing'):
            kanban.status = 1
        else:
            kanban.status = 2
        kanban.date_end = request.POST['date_end']
        kanban.introduce = request.POST['introduce']

        kanban.save()

        return redirect(
            resolve_url('kanban', p_pk)
        )

    #변경안된 경우
    return render(
        request,
        'team_kanban/rewritekanban.html',
        {
            'post':project,
            'kanban':kanban,
            'participants': participants,
        }
    )

def delete_kanban(request, p_pk, s_pk, i_pk):
    project = Project.objects.get(pk=p_pk)  # 프로젝트의 pk값
    kanban = Kanban.objects.get(team=project.team, pk=i_pk)

    kanban.delete()

    return redirect(
        resolve_url('kanban', p_pk)
    )


