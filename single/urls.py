from django.urls import path, include
from . import views

urlpatterns=[
    #시간표(single)
    path('', views.single_day),
    #캘린더(sigle/calender)
    path('calender/', views.single_cal),
    #edit창
    path('create_post/', views.single_edit),
]