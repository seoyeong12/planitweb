from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, resolve_url

from . import models
from .models import Project, Team, Participant  # 프로젝트 모델 import
# Create your views here.

def create_team(request):
    team = models.Team()
    user = User.objects.get(email=request.user.email)

    if request.method == 'POST':
        team.team_name = request.POST['team']
        team.save()
        try:
            User.objects.get(email=request.POST['user1'])
        except:
            # user1의 아이디가 user에 없는 경우 or 입력을 안한 경우 -> 해당하는 participant는 삭제
            # 계정이 존재하지 않음 -> 회원가입 메세지 보내기
            print("")
        else:
            participant = models.Participant()
            participant.team = team
            participant.user = user
            participant.save()

        try:
            User.objects.get(email=request.POST['user2'])
        except:
            # user1의 아이디가 user에 없는 경우 or 입력을 안한 경우 -> 해당하는 participant는 삭제
            # 계정이 존재하지 않음 -> 회원가입 메세지 보내기
            print("")
        else:
            participant = models.Participant()
            participant.team = team
            participant.user = User.objects.get(email=request.POST['user2'])
            participant.save()

        try:
            User.objects.get(email=request.POST['user3'])
        except:
            # user1의 아이디가 user에 없는 경우 or 입력을 안한 경우 -> 해당하는 participant는 삭제
            # 계정이 존재하지 않음 -> 회원가입 메세지 보내기
            print("")
        else:
            participant = models.Participant()
            participant.team = team
            participant.user = User.objects.get(email=request.POST['user3'])
            participant.save()

        try:
            User.objects.get(email=request.POST['user4'])
        except:
            # user1의 아이디가 user에 없는 경우 or 입력을 안한 경우 -> 해당하는 participant는 삭제
            # 계정이 존재하지 않음 -> 회원가입 메세지 보내기
            print("")
        else:
            participant = models.Participant()
            participant.team = team
            participant.user = User.objects.get(email=request.POST['user4'])
            participant.save()

        try:
            User.objects.get(email=request.POST['user5'])
        except:
            # user1의 아이디가 user에 없는 경우 or 입력을 안한 경우 -> 해당하는 participant는 삭제
            # 계정이 존재하지 않음 -> 회원가입 메세지 보내기
            print("")
        else:
            participant = models.Participant()
            participant.team = team
            participant.user = User.objects.get(email=request.POST['user5'])
            participant.save()

        return redirect(resolve_url('create_project'))

    else:
        return render(
            request,
            'team_project/userplus.html',
            {
                'team':team,
                'author':user,
            }
        )

def create_project(request):
    user = User.objects.get(username=request.user.username)
    #팀 데이터가 없는 경우
    if Team.objects.all().count() == 0:
        return render(
            request,
            'team_project/teamproject_write.html',
            {
                'prev_project': 0,
            }
        )
    else:
        #팀 데이터가 있는 경우
        #최근 값을 가져온다
        team = Team.objects.latest('pk')  # 가장 최근 값
        participants = Participant.objects.filter(team=team)  # 최근 값에 해당하는 프로젝트가 있다
        try:
            prev_project = Project.objects.get(team=team)  # 최근 값에 해당하는 프로젝트가 없는 경우
        except:
            #프로젝트를 만들어야 한다
            project = models.Project()
            t_participants = Participant.objects.filter(project=None)  # 최근 값에 해당하는 프로젝트가 없다

            if request.method == 'POST':
                project.team = Team.objects.latest('pk')
                project.title = request.POST['title']
                project.date_start = request.POST['date_start']
                project.date_end = request.POST['date_end']
                project.introduce = request.POST['introduce']
                project.author = user

                project.save()

                for p in t_participants:
                    p.project = project
                    p.save()
                return redirect(resolve_url('main'))
            else:
                return render(
                    request,
                    'team_project/teamproject_write.html',
                    {
                        'team': team,
                        'prev_project': 1,
                        'participants': participants,

                    }
                )
        else:  # 최근 값에 해당하는 프로젝트가 있는 경우 -> 새로 만드는 화면
            return render(
                request,
                'team_project/teamproject_write.html',
                {
                    'team': team,
                    'prev_project': 0,
                }
            )
def index(request):
    user = User.objects.get(username=request.user.username)
    posts = Participant.objects.filter(user=user).order_by('-pk') #프로젝트 모델의 레코드 최신순으로 정렬

    return render(
        request,
        'team_project/index.html',
        {
            'posts': posts, #가져온 레코드 리턴
        })


def detail(request, p_pk):
    post = Project.objects.get(pk=p_pk)#pk에 해당하는 모델의 레코드를 get
    participants = Participant.objects.filter(team=post.team)
    return render(
        request,
        'team_project/teamproject_intro.html',
        {
            'post': post,  # 가져온 레코드 리턴
            'participants': participants,
        }
    )


def delete_team(request, p_pk):
    post = Project.objects.get(pk=p_pk)
    team = Team.objects.get(pk=post.team.pk)
    # delete 에서 프로젝트 없는 팀 삭제해야함
    team.delete()
    return redirect(
        resolve_url('main')
    )


def rewrite_project(request, p_pk):
   post = Project.objects.get(pk=p_pk)
   participants = Participant.objects.filter(team=post.team)
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
                         'participants': participants,
                     })

