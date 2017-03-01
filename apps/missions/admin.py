from django.contrib import admin

from .models import Missions


class MissionsAdmin(admin.StackedInline):
    model = Missions
    can_delete = False
    verbose_name_plural = 'Missions'


admin.site.register(Missions)
