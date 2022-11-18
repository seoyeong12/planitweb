from django.urls import path
from . import views

urlpatterns = [
    #path('<int:pk>/log/', include('team_log.urls')),#백로그
    path('', views.index, name='log'),
    path('<int:l_pk>/', views.update_log, name='update_log'),#추가
    #path('<int:l_pk>/delete', views.delete_log, name='delete_log'),#삭제
]