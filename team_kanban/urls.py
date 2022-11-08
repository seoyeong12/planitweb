from django.urls import path
from . import views

urlpatterns = [
    #path('<int:pk>/kanban/', include('team_kanban.urls')),#칸반
    path('', views.index),#칸반
    path('<int:pk>/', views.detail),
]