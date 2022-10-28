from django.shortcuts import render
from .models import Log
from team_project.models import Project

# Create your views here.

def index(request, pk):
    post = Project.objects.get(pk=pk)
    logs = Log.objects.filter(team=post.pk)

    return render(
        request,
        'team_log/backlog.html',
        {
            'post':post,
            'log': logs,
        })