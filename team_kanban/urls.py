from django.urls import path
from . import views

urlpatterns = [
    #path('<int:pk>/kanban/', include('team_kanban.urls')),#칸반
    path('', views.index, name='kanban'),#프로젝트의 모든 칸반
    path('<int:s_pk>/create_kanban/', views.create_kanban, name='create_kanban'),#목록페이지에서 칸반 생성
    path('<int:s_pk>/<int:i_pk>/', views.detail, name='inside_kanban'),#칸반 상세 페이지
    path('<int:s_pk>/<int:i_pk>/rewrite_kanban', views.rewrite_kanban, name='rewrite_kanban'),#칸반 수정 페이지
    path('<int:s_pk>/<int:i_pk>/delete_kanban', views.delete_kanban, name='delete_kanban'),#칸반 삭제 페이지
]