from django.urls import path

from team_user import views

urlpatterns=[
    path('', views.signup, name='signup'),
    path('', views.signin, name='signin'),
]