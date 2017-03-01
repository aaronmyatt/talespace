from rest_framework import serializers

from .models import Missions


class MissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Missions
        fields = ['user', 'name', 'mission']
