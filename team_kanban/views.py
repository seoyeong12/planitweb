from django.shortcuts import render, redirect, resolve_url

# Create your views here.
from team_kanban import models
from team_kanban.models import Kanban
from team_project.models import Project

#칸반 생성
#http://127.0.0.1:8000/team/프로젝트pk값/kanban/프로젝트 상태 pk값/create_kanban
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
        #저장 후 창 닫고 상위 페이지가 새로고침 되어야함
        return redirect(resolve_url('kanban', p_pk))

    return render(
        request,
        'team_kanban/writekanban.html',
        {
            'status':kanban_status,
        }
    )

#기존의 칸반 보여줌
#http://127.0.0.1:8000/team/프로젝트pk/kanban/
def index(request, p_pk):
    project = Project.objects.get(pk=p_pk)#프로젝트의 pk값
    todo = Kanban.objects.filter(team=project, status=0)
    doing = Kanban.objects.filter(team=project, status=1)
    done = Kanban.objects.filter(team=project, status=2)


#    if request.method == 'POST':


    return render(
        request,
        'team_kanban/kanban.html',
        {
            'post':project,
            'todo':todo,
            'doing':doing,
            'done':done
        }
    )

#칸반 상세 페이지
#http://127.0.0.1:8000/team/프로젝트 pk값/kanban/프로젝트의 상태 pk값/데이터베이스pk값/
def detail(request, p_pk, s_pk, i_pk):
    project = Project.objects.get(pk=p_pk)  # 프로젝트의 pk값
    kanban = Kanban.objects.get(team=project, pk=i_pk)
    todo = Kanban.objects.filter(team=project, status=s_pk).get(pk=i_pk)
    doing = Kanban.objects.filter(team=project, status=s_pk).get(pk=i_pk)
    done = Kanban.objects.filter(team=project, status=s_pk).get(pk=i_pk)


    return render(
        request,
        'team_kanban/insidekanban.html',
        {
            'post':project,
            'kanban':kanban,
            'todo': todo,
            'doing': doing,
            'done': done
        }
        )

def rewrite_kanban(request, p_pk, s_pk, i_pk):
    project = Project.objects.get(pk=p_pk)  # 프로젝트의 pk값
    kanban = Kanban.objects.get(team=project, pk=i_pk)

    #변경된 경우
    if request.method == 'POST':
        kanban.team = project  #고정
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
        }
    )

def delete_kanban(request, p_pk, s_pk, i_pk):
    project = Project.objects.get(pk=p_pk)  # 프로젝트의 pk값
    kanban = Kanban.objects.get(team=project, pk=i_pk)

    kanban.delete()

    return redirect(
        resolve_url('kanban', p_pk)
    )


