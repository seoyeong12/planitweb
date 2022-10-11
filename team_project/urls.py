from django.urls import path
from . import views

#crete_team
urlpatterns = [
    path('', views.index),#프로젝트 모아보기
    path('team_detail', views.detail)#프로젝트 상세 보기..? 메인 디자인에 따라서 달라짐
]