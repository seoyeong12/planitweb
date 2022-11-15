from django.urls import path
from . import views

urlpatterns= [
    #로그인(sign/in)
    path('in', views.signin),
    #회원가입(sign/up)
    path('up', views.signup),
]

