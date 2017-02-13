from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from apps.authentication.models import Volunteer, Mission


class VolunteerInline(admin.StackedInline):
    model = Volunteer
    can_delete = False
    verbose_name_plural = 'Volunteers'

class MissionInline(admin.StackedInline):
    model = Mission
    can_delete = False
    verbose_name_plural = 'Missions'


class UserAdmin(BaseUserAdmin):
    inlines = (VolunteerInline, MissionInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
