from django.db import models

# Create your models here.
import team_project.models

class Log(models.Model):
    # 팀 프로젝트와 다대일 관계(하나의 팀은 여러 회의 노트를 가질 수 있다.)
    team = models.ForeignKey(team_project.models.Team, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    title = models.CharField(max_length=50)

    #나중에 views.py 로 옮기기
    def __str__(self):
        if self.status == True:
            return f'[{self.id}] {self.title} [True]'
        else:
            return f'[{self.id}] {self.title} [False]'