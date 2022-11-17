"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin/', include('team_user.urls')),
    path('team/', include('team_project.urls')),#더 좋은 url 찾는 중
    #미팅 노트
    #path('meeting_note/', include('team_meetingnote.urls')),
    #칸반
    #path('kanban/', include('team_kanban.urls')),
    #로그
    #path('log/', include('team_log.urls')),
    #스케쥴/달력
    path('single/', include('single.urls')),
    #로그인/회원가입
    # path('sign/', include('user.urls')),
    #edit
    path('edit/', include('single.urls')),
]
