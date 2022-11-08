from django.db import models

# Create your models here.
import team_project.models

class Kanban(models.Model):
    TODO = 0
    DOING = 1
    DONE = 2
    STATUS = (
        (TODO, 'todo'),
        (DOING, 'doing'),
        (DONE, 'done')
    )

    # 팀 프로젝트와 다대일 관계(하나의 팀은 여러 회의 노트를 가질 수 있다.)
    team = models.ForeignKey(team_project.models.Project, on_delete=models.CASCADE)
    status = models.SmallIntegerField(default=0, choices=STATUS)
    title = models.CharField(max_length=30)
    date_end = models.DateField()
    introduce = models.TextField()
    # user와 team 테이블 생성시 작성
    # participants = models.BooleanField(default=True)

    def __str__(self):
        return f'[{self.team}] {self.title}'

    #def get_absolute_url(self):
    #    return f'/create_team/{self.pk}/'