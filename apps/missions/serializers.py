from rest_framework import serializers
from apps.skills.models import Skills
from .models import Missions, MissionRequiresSkills
from apps.users.serializers import UserSerializer


class MissionSerializer(serializers.ModelSerializer):
    description = serializers.CharField(required=False)
    user = UserSerializer(required=False)

    class Meta:
        model = Missions
        fields = ['user', 'name', 'description', 'skills']

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'

class MissionSkillsSerializer(serializers.ModelSerializer):
    skill = SkillsSerializer()
    
    class Meta:
        model = MissionRequiresSkills
        fields = ['mission', 'skill', 'level']
