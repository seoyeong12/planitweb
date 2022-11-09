from django.db import models
# Create your models here.
class Schedule(models.Model) :
    SINGLE = 0
    TEAM = 1
    STATUS = (
        (SINGLE, 'single'),
        (TEAM, 'team')
    )
    how = models.SmallIntegerField(default=0, choices=STATUS)
    date = models.DateField()
    startTime = models.TimeField()
    dueTime = models.TimeField()
    title = models.CharField(max_length=50, default="")
    image = models.ImageField(upload_to='profile', null=True)

    def __str__(self):
        return f'[{self.pk}] {self.title}'

    def get_absolute_url(self):
        return f'/single/create_post'