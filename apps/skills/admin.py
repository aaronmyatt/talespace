from django.contrib import admin

from .models import Skills


class SkillsAdmin(admin.StackedInline):
    model = Skills
    can_delete = False
    verbose_name_plural = 'Missions'


admin.site.register(Skills)
