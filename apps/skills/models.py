from django.db import models


class Skills(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300, default='')
