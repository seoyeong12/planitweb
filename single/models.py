from django.db import models
from django.shortcuts import get_object_or_404
from django.views import View


# Create your models here.
class Schedule(models.Model) :
    SINGLE = 0
    TEAM = 1
    STATUS = (
        (SINGLE, 'single'),
        (TEAM, 'team')
    )
    how = models.SmallIntegerField(default=0, choices=STATUS, null=True)
    team = models.ForeignKey('team_project.Team', on_delete=models.SET_NULL, null=True, blank=True, default=None)
    date = models.DateField(null=True)
    startTime = models.TimeField(null=True)
    dueTime = models.TimeField(null=True)
    title = models.CharField(max_length=50, default="")

    def __str__(self):
        return f'[{self.pk}] {self.title}'

    def get_absolute_url(self):
        return f'/single/create_post'