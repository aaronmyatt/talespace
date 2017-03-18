from rest_auth.views import UserDetailsView
from rest_framework.viewsets import ModelViewSet

from .models import UserDetails, UserSkills
from .serializers import UserSkillsSerializer


class CustomUserDetailsView(UserDetailsView):

    def get_object(self):
        user = self.request.user
        return UserDetails.objects.get(user=user)

    def update(self, request, *args, **kwargs):
        return super().update(request, partial=True)


class UserSkillsView(ModelViewSet):
    '''
    Gets the users skills
    TODO: limit single object lookup to the users skills only!
    '''
    queryset = UserSkills.objects.all()
    serializer_class = UserSkillsSerializer

    def get_queryset(self):
        return UserDetails.objects.get(user=self.request.user).userskills_set

    def perform_create(self, serializer):
        user = self.request.user
        user_details = UserDetails.objects.get(user=user)
        serializer.save(user=user_details)
