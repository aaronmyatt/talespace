from django.conf import settings
from django.db import models

from apps.skills.models import Skills


# Create your models here.


class Missions(models.Model):
    user        = models.ForeignKey(to=settings.AUTH_USER_MODEL)
    name        = models.CharField(max_length=100)
    description = models.TextField()
    skills = models.ManyToManyField(Skills, through='MissionRequiresSkills')


class MissionRequiresSkills(models.Model):
    CHOICES = [(i, i) for i in range(6)]

    mission = models.ForeignKey(Missions)
    skill = models.ForeignKey(Skills)
    level = models.IntegerField(choices=CHOICES)
