from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),#프로젝트 모아보기 html 아직 미완성
    path('<int:pk>/', views.detail),#프로젝트 상세 보기..? 메인 디자인에 따라서 달라짐
    path('<int:pk>/meeting_note/', include('team_meetingnote.urls')),
    path('<int:pk>/kanban/', include('team_kanban.urls')),#칸반
    path('<int:pk>/log/', include('team_log.urls')),#백로그
]