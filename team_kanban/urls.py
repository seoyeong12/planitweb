from django.urls import path
from . import views

urlpatterns = [
    #path('<int:pk>/kanban/', include('team_kanban.urls')),#칸반
    path('', views.index, name='kanban'),#프로젝트의 모든 칸반
    path('<int:s_pk>/create_kanban/', views.create_kanban, name='create_kanban'),
    path('<int:pk>/', views.detail),
]