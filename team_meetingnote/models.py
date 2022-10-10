from django.db import models

# Create your models here.
import team_project.models


class Note(models.Model):
    # 팀 프로젝트와 다대일 관계(하나의 팀은 여러 회의 노트를 가질 수 있다.)
    # note_id = models.ForeignKey(team_project.models.Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    date_start = models.DateField()
    introduce = models.TextField()
    participants = models.BooleanField(default=True)

