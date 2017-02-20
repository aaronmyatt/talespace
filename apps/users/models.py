from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserDetails(models.Model):

    USER_TYPES = (
        ('v', 'volunteer'),
        ('m', 'mission'),
    )

    user         = models.OneToOneField(to=settings.AUTH_USER_MODEL)
    user_type    = models.CharField(max_length=1, choices=USER_TYPES)
    company_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    school = models.CharField(max_length=100)
    description  = models.TextField()
    experience   = models.TextField()
    interests    = models.TextField()
    languages    = models.TextField()
    website      = models.URLField()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, created, instance, **kw):
    if created:
        ud = UserDetails()
        ud.user = instance
        ud.save()

