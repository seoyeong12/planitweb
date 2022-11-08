from django.urls import path
from . import views


urlpatterns = [
    #path('<int:pk>/meeting_note/', include('team_meetingnote.urls')),
    path('', views.index, name='meeting_list'),#회의록 목록 보기
    path('create_note/', views.create_note, name='create_note'),#회의록 작성하기
    path('<int:pk>/', views.detail, name='detail'),#회의록 상세 보기
    path('<int:pk>/rewrite_note/', views.rewrite_note, name='rewrite_note'),#회의록 수정하기
    path('<int:pk>/delete_note/', views.delete_note, name='delete_note'),#회의록 삭제하기
]
