from django.shortcuts import render
from django.views.generic import CreateView

from .models import Project #프로젝트 모델 import
# Create your views here.


class CreatePost(CreateView):
    # 프로젝트 모델을 통해 프로젝트 생성한다.
    model = Project
    #팀원을 불러오기
    #팀원 = team과 user의 조인 테이블에 해당
    fields = ['title', 'date_start', 'date_end', 'introduce']

def index(request):
    posts = Project.objects.all().order_by('-pk')#프로젝트 모델의 레코드 최신순으로 정렬

    return render(
        request,
        'team_project/index.html',
        {
            'posts': posts, #가져온 레코드 리턴
        })


def detail(request, pk):
    post = Project.objects.get(pk=pk)#pk에 해당하는 모델의 레코드를 get

    return render(
        request,
        'team_project/teamproject_intro.html',
        {
            'post': post,  # 가져온 레코드 리턴
        }
    )

