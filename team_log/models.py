from django.db import models

# Create your models here.

class Log(models.Model):
    # 팀 프로젝트와 다대일 관계(하나의 팀은 여러 회의 노트를 가질 수 있다.)
    # note_id = models.ForeignKey(team_project.models.Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    status = models.BooleanField(default=True)

    #나중에 views.py 로 옮기기
    def __str__(self):
        if self.status == True:
            return f'[{self.id}] {self.title} [True]'
        else:
            return f'[{self.id}] {self.title} [False]'