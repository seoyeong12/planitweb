from django.shortcuts import render, redirect

from .models import Schedule
from django.views.generic import CreateView
# Create your views here.

def single_day(request):
    schedules = Schedule.objects.all().order_by('date', 'startTime')
    return render(
        request,
        'single/days.html',
        {
            'schedules' : schedules
        }
    )

def single_cal(request):
    return render(
        request,
        'single/calender.html',
    )

def single_edit(request):
    return render(
        request,
        'single/schedule_form.html',
    )

# def post_create(request):
#     if request.method == 'POST':
#         form = PostCreateForm(request.POST)
#         if form.is_valid():
#             Schedule= form.save(commit=False)
#             Schedule.title = request.user
#             return redirect('days', id=Schedule.id)
#     else:
#         form = PostCreateForm()
#     return render(request, 'single/post_create.html', {'form':form})