from django.urls import path
from . import views

urlpatterns = [
    #path('<int:pk>/log/', include('team_log.urls')),#백로그
    path('', views.index),
    path('create_log/', views.CreateLog.as_view())
]