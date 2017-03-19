from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from .models import Missions, MissionRequiresSkills
from .serializers import MissionSerializer, MissionSkillsSerializer


class MissionModelView(ModelViewSet):

    queryset = Missions.objects.all()
    serializer_class = MissionSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
    
    @detail_route()
    def required_skills(self, request, pk):
        mission_skill_subset = MissionRequiresSkills.objects.filter(mission=pk)
        serializer = MissionSkillsSerializer(mission_skill_subset, many=True)
        return Response(serializer.data)


class MissionSkillsView(ModelViewSet):

    queryset = MissionRequiresSkills.objects.all()
    serializer_class = MissionSkillsSerializer

