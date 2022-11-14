from django.shortcuts import render, redirect, resolve_url

from . import models
from .models import Project, Team  # 프로젝트 모델 import
# Create your views here.

def create_team(request):
    team = models.Team()

    if request.method == 'POST':
        team.team_name = request.POST['team']
        team.save()

        return redirect(resolve_url('create_project'))

    else:
        return render(
            request,
            'team_project/userplus.html',
            {
                'team':team,
            }
        )
 #delete 에서 프로젝트 없는 팀 삭제해야함
def create_project(request):
    team = Team.objects.latest('pk') #가장 최근 값
    #prev_project = Project.objects.get(team=team.pk)#가장 최근 값에 해당하는 프로젝트
    project = models.Project()

    try:
        prev_project = Project.objects.get(team=team) #최근 값에 해당하는 프로젝트가 없는 경우
    except:
        if request.method == 'POST':
            project.team = Team.objects.latest('pk')
            project.title = request.POST['title']
            project.date_start = request.POST['date_start']
            project.date_end = request.POST['date_end']
            project.introduce = request.POST['introduce']

            project.save()
            return redirect(resolve_url('main'))
        else:
            return render(
                request,
                'team_project/teamproject_write.html',
                {
                    'team': team,
                    'prev_project': 1,
                    'project': project,

                }
            )
    else: #최근 값에 해당하는 프로젝트가 있는 경우
        return render(
            request,
            'team_project/teamproject_write.html',
            {
                'team': team,
                'prev_project': 0,
                'project': project,

            }
        )

def index(request):
    posts = Project.objects.all().order_by('-pk')#프로젝트 모델의 레코드 최신순으로 정렬

    return render(
        request,
        'team_project/index.html',
        {
            'posts': posts, #가져온 레코드 리턴
        })


def detail(request, p_pk):
    post = Project.objects.get(pk=p_pk)#pk에 해당하는 모델의 레코드를 get

    return render(
        request,
        'team_project/teamproject_intro.html',
        {
            'post': post,  # 가져온 레코드 리턴
        }
    )

def rewrite_project(request, p_pk):
   post = Project.objects.get(pk=p_pk)

   if request.method == 'POST':
       post.title = request.POST['title']
       post.date_start = request.POST['date_start']
       post.date_end = request.POST['date_end']
       post.introduce = request.POST['introduce']

       post.save()
       return redirect(resolve_url('project_detail', p_pk))

   else:
       return render(request,
                     'team_project/teamproject_rewrite.html',
                     {
                         'post':post,
                     })



