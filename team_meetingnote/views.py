from django.shortcuts import render
from .models import Note
from team_project.models import Project

# Create your views here.

def index(request, pk):
    post = Project.objects.get(pk=pk)
    notes = Note.objects.all()

    return render(
        request,
        'team_meetingnote/proceedings.html',
        {
            'post':post,
            'notes':notes,
        })

def detail(request, pk):
    note = Note.objects.get(pk=pk)

    return render(
        request,
        'team_meetingnote/proceedings_detail.html',
        {
            'note':note,
        }
    )