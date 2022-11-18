from django.contrib import admin
from .models import Project, Team, Participant

# Register your models here.

admin.site.register(Project)
admin.site.register(Team)
admin.site.register(Participant)
