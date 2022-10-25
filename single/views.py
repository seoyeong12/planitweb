from django.shortcuts import render

# Create your views here.

def single_day(request):
    return render(
        request,
        'single/days.html',
    )

def single_cal(request):
    return render(
        request,
        'single/calender.html',
    )