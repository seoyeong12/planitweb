from django.urls import path
from . import views

#app_name = ''

urlpatterns= [
    #로그인(sign/in)
    path('signin/', views.signin, name='signin'),

    #로그아웃(sign/in)
    path('signout/', views.signout, name='signout'),

    #회원가입(sign/up)
    path('signup/', views.signup, name='signup'),
]

