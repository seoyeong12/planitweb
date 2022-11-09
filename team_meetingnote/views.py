from django.shortcuts import render, redirect, resolve_url
from django.urls import reverse
from django.views.generic import CreateView

from . import models
from .models import Note
from team_project .models import Project

# Create your views here.

#class CreateNote(CreateView):
#    model = Note
#    fields = ['team', 'title', 'date_start', 'introduce']
#    template_name = 'team_meetingnote/proceedings_write.html'

#post 입력이 안되는 경우 -> 에러 메세지 출력하는 함수 필요하다.

def create_note(request, pk):
    post = Project.objects.get(pk=pk)
    note = models.Note()

    if request.method == 'POST':
        note.team = post.team
        note.title = request.POST['title']
        note.date_start = request.POST['date_start']
        note.introduce = request.POST['introduce']

        note.save()
        return redirect(resolve_url('meeting_list', post.id))

    return render(
        request,
        'team_meetingnote/proceedings_write.html',
    )

def rewrite_note(request, pk):
    note = Note.objects.get(pk=pk)

#변경된 경우
    if request.method == 'POST':
        note.title = request.POST['title']
        note.date_start = request.POST['date_start']
        note.introduce = request.POST['introduce']

        note.save()
        return redirect(resolve_url('meeting_list', note.team.project.id))

#변경 안된 경우 그냥 기존의 detail 페이지 보여주기
    else:
        return render(
        request,
        'team_meetingnote/proceedings_rewrite.html',{
                'note':note,
            }
        )

def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    note.delete()
    return redirect(resolve_url('meeting_list', note.team.project.id))

def index(request, pk):
    post = Project.objects.get(pk=pk)
    #해당 프로젝트의 타이틀
    #해당 프로젝트의 pk값
    #그 pk값에 해당하는 노트들 필요
    notes = Note.objects.filter(team=post.team).order_by('date_start')

    return render(
        request,
        'team_meetingnote/proceedings.html',
        {
            'post':post,
            'notes':notes,
        })

def detail(request, pk):
    note = Note.objects.get(pk=pk) #수정해야할듯..?

    return render(
        request,
        #'team_meetingnote/index.html',
        'team_meetingnote/proceedings_detail.html',
        {
            'note':note,
        }
    )