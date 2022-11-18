from django.urls import path

from team_user import views

urlpatterns=[
    path('', views.signin, name='signup'),
    path('signup/', views.signup, name='view.signup'),
]