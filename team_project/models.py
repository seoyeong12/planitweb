from django.db import models

# Create your models here.

class Team(models.Model):
    team_name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.team_name}'


class Project(models.Model):
    team = models.OneToOneField(Team, on_delete=models.CASCADE, null='개인') #팀 모델과 일대일 관계
    title = models.CharField(max_length=30)
    date_start = models.DateField()
    date_end = models.DateField()
    introduce = models.TextField()

    def __str__(self):
        return f'[{self.pk}] {self.title}'

    def get_absolute_url(self):
        return f'/create_team/{self.pk}/'