from django.contrib.auth import get_user_model
from apps.users.models import UserDetails
from rest_auth.registration import serializers as rest_auth_serializers
from rest_framework import serializers

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


class UserDetailsSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserDetails
        fields = '__all__'
