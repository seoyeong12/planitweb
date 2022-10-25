from django.db import models

# Create your models here.

class Team(models.Model):
    team_name = models.CharField(max_length=30, default="")
class User(models.Model) :
    team = models.ForeignKey(Team, on_delete=models.SET_NULL,null=True)
    user_name = models.CharField(max_length=10, default="")
    email = models.EmailField(default="")
    password = models.CharField(max_length=50, default="", verbose_name="비밀번호")
    first_name = models.CharField(max_length=10, default="")
    last_name = models.CharField(max_length=10, default="")

    def __str__(self):
        return f'[{self.pk}] {self.user_name}'