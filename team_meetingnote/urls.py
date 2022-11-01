from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),#회의록 목록 보기
    path('<int:pk>/', views.detail),#회의록 상세 보기
    path('create_note/', views.CreateNote.as_view()),#회의록 작성하기
]