from django.urls import path

from team_user import views

urlpatterns=[
    path('', views.signin, name='signin'),#로그인
    path('signup/', views.signup, name='signup'),#회원가입
]