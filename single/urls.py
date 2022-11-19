from django.urls import path
from . import views

urlpatterns=[
    #시간표(single)
    path('', views.single_day, name='single'),
    #캘린더(single/calender)
    path('calender/', views.single_cal, name='calendar'),
    #edit창
    path('create_post/', views.single_edit, name='post'),
    #상세 페이지
    path('detail_post/<int:pk>/', views.single_detail, name='detail'),
    #수정페이지
    path('modify_post/<int:pk>/',views.single_modify, name='modify'),
    #삭제페이지
    path('delete_post/<int:pk>/', views.single_delete, name='delete'),
]