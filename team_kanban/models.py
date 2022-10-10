from django.db import models

# Create your models here.

class Kanban(models.Model):
    # 팀 모델과 일대일 관계
    # band_id = models.OneToOneField(team.Team, on_delete=models.CASCADE) 추후 작성
    # 팀 모델과 다대일 관계(하나의 팀은 여러 회의 노트를 가질 수 있다.)
    # kanban_id = models.ForeignKey(team_project.models.Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    date_end = models.DateField()
    introduce = models.TextField()
    participants = models.BooleanField(default=True)