from django.urls import path
import team_meetingnote.views
import team_kanban.views
import team_log.views
from . import views

urlpatterns = [
    path('', views.index),#프로젝트 모아보기 html 아직 미완성
    path('<int:pk>/', views.detail),#프로젝트 상세 보기..? 메인 디자인에 따라서 달라짐
    path('<int:pk>/meeting_note/', team_meetingnote.views.index),#회의록
    path('<int:pk>/kanban/', team_kanban.views.index),#칸반
    path('<int:pk>/log/', team_log.views.index),#백로그
]