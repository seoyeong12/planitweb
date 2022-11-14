from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='main'),#프로젝트 모아보기 html 아직 미완성
    path('<int:p_pk>/', views.detail, name='detail'),#프로젝트 상세 보기..? 메인 디자인에 따라서 달라짐
    path('create_project/', views.create_project, name='create_project'),#프로젝트 상세 보기..? 메인 디자인에 따라서 달라짐
    path('create_project/create_team/', views.create_team, name='create_team'),#프로젝트 상세 보기..? 메인 디자인에 따라서 달라짐
    path('<int:p_pk>/meeting_note/', include('team_meetingnote.urls'), name='meetingnote'),#회의록
    path('<int:p_pk>/kanban/', include('team_kanban.urls'), name='kanban'),#칸반
    path('<int:pk>/log/', include('team_log.urls'), name='log'),#백로그
]