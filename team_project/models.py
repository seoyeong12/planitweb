from django.db import models

# Create your models here.

#팀 프로젝트 메인 페이지
class Project(models.Model):
    #팀 모델과 일대일 관계
    #band_id = models.OneToOneField(team.Team, on_delete=models.CASCADE) 추후 작성
    title = models.CharField(max_length=30)
    date_start = models.DateField()
    date_end = models.DateField()
    introduce = models.TextField()

    def __str__(self):
        return f'[{self.pk}] {self.title}'
