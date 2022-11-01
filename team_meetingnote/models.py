from django.db import models
import team_project.models
# Create your models here.


class Note(models.Model):
    # 팀 프로젝트와 다대일 관계(하나의 팀은 여러 회의 노트를 가질 수 있다.)
    team = models.ForeignKey(team_project.models.Team, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    date_start = models.DateField()
    introduce = models.TextField()
    #user와 team 테이블 생성시 작성
    #participants = models.BooleanField(default=True)

    def __str__(self):
        return f'[{self.pk}] {self.title}'

    #def get_absolute_url(self):
    #    return f'/create_team/{self.pk}/'
