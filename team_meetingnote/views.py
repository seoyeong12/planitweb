from django.shortcuts import render, redirect, resolve_url

from . import models
from .models import Note
from team_project.models import Project, Participant


# Create your views here.


def create_note(request, p_pk):
    post = Project.objects.get(pk=p_pk)
    participants = Participant.objects.filter(team=post.team)

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
        {
            'participants':participants,
        }
    )

def rewrite_note(request,p_pk, i_pk):
    post = Project.objects.get(pk=p_pk)
    note = Note.objects.filter(team=post.team).get(pk=i_pk)
    participants = Participant.objects.filter(team=post.team)

#변경된 경우
    if request.method == 'POST':
        note.title = request.POST['title']
        note.date_start = request.POST['date_start']
        note.introduce = request.POST['introduce']

        note.save()
        return redirect(resolve_url('meeting_list', p_pk))

#변경 안된 경우 그냥 기존의 detail 페이지 보여주기
    else:
        return render(
        request,
        'team_meetingnote/proceedings_rewrite.html',{
                'note':note,
                'participants': participants,
            }
        )

def delete_note(request, p_pk, i_pk):
    post = Project.objects.get(pk=p_pk)
    note = Note.objects.filter(team=post.team).get(pk=i_pk)

    note.delete()
    return redirect(resolve_url('meeting_list', note.team.project.id))

def index(request, p_pk):
    post = Project.objects.get(pk=p_pk)
    notes = Note.objects.filter(team=post.team).order_by('date_start')

    return render(
        request,
        'team_meetingnote/proceedings.html',
        {
            'post':post,
            'notes':notes,
        })

def detail(request, p_pk, i_pk):
    post = Project.objects.get(pk=p_pk)
    note = Note.objects.filter(team=post.team).get(pk=i_pk)
    participants = Participant.objects.filter(team=post.team)

    return render(
        request,
        'team_meetingnote/proceedings_detail.html',
        {
            'post':post,
            'note':note,
            'participants':participants,
        }
    )