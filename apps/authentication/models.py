"""User Models"""

from django.contrib.auth.models import User
from django.db import models


class Skill(models.Model):
    """Helper Model that has `ManyToMany` relationship to `Volunteer`

    so it is easy to store multiple skills
    for one volunteer.
    """
    skill = models.CharField(max_length=70)

class Volunteer(models.Model):
    """Volunteer user model that has `OneToOne` relationship with the built in `User` model"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skils = models.ManyToManyField(Skill)
    is_volunteer = models.BooleanField(default=False)


class Mission(models.Model):
    """Mission user model that has `OneToOne` relationship with the built in `User` model"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=150)
    volunteers = models.ManyToManyField(Volunteer)
    is_mission = models.BooleanField(default=False)
