from django.db import models
from django.conf import settings

# Create your models here.


class Missions(models.Model):

    user        = models.ForeignKey(to=settings.AUTH_USER_MODEL)
    name        = models.CharField(max_length=100)
    description = models.TextField()

