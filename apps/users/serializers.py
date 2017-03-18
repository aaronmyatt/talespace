from django.contrib.auth import get_user_model
from rest_auth.registration import serializers as rest_auth_serializers
from rest_framework import serializers

from apps.skills.models import Skills
from apps.users.models import UserDetails, UserSkills

UserModel = get_user_model()

class UserRegistrationSerializer(rest_auth_serializers.RegisterSerializer):
    user_type = serializers.CharField(max_length=1,
                                      default='v',
                                      allow_blank=True)

    def custom_signup(self, request, user):
        user_details = UserDetails.objects.get(user=user)
        utype = self.validated_data.get('user_type', 'v')
        user_details.user_type = utype
        user_details.save()

    def validate_user_type(self, user_type):
        if user_type:
            return user_type
        return 'v'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ('pk', 'username', 'email', 'first_name', 'last_name')
        read_only_fields = ('email', )


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'


class UserSkillsSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=UserDetails.objects.all(),
                                              required=False)

    class Meta:
        model = UserSkills
        fields = ['user', 'skill', 'level']


class UserDetailsSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    skills = UserSkillsSerializer(source='userskills_set', many=True, read_only=True)

    class Meta:
        model = UserDetails
        fields = '__all__'
