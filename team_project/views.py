from django.shortcuts import render

# Create your views here.

def index(request):
    return render(
        request,
        'team_project/index.html')


def detail(request):
    return render(
        request,
        'team_project/detail.html')

