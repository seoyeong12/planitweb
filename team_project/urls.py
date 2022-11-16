from django.urls import path, include
from . import views

#p_pk = 프로젝트의 pk값이 된다
urlpatterns = [
    path('', views.index, name='main'),#프로젝트 모아보기 html 아직 미완성
    path('create_project/', views.create_project, name='create_project'),  # 프로젝트 생성
    path('create_project/create_team/', views.create_team, name='create_team'),  # 팀 생성, 팀원 추가

    path('<int:p_pk>/', views.detail, name='project_detail'),#프로젝트 상세 보기..? 메인 디자인에 따라서 달라짐
    path('<int:p_pk>/rewrite_project/', views.rewrite_project, name='rewrite_project'), #프로젝트 수정
    path('<int:p_pk>/delete_project/', views.delete_team, name='delete_team'),#팀 삭제
    path('<int:p_pk>/plus_user/', views.plus_user, name='plus_user'),#팀원 추가
    #path('<int:p_pk>/delete_user/', views.delete_user, name='delete_user'),#팀원 삭제

    path('<int:p_pk>/meeting_note/', include('team_meetingnote.urls'), name='meetingnote'),#회의록
    path('<int:p_pk>/kanban/', include('team_kanban.urls'), name='kanban'),#칸반
    path('<int:pk>/log/', include('team_log.urls'), name='log'),#백로그
]