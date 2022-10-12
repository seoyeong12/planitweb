from django.db import models

# Create your models here.
class Schedule(models.Model) :
    single = models.BooleanField(default=False)
    team = models.BooleanField(default=False)
    date = models.DateField()
    startTime = models.TimeField()
    dueTime = models.TimeField()
    title = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.title
