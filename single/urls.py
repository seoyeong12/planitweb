from django.urls import path
from . import views

urlpatterns=[
    path('', views.single_day),
    path('calender', views.single_cal)
]