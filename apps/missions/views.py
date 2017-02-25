from rest_framework.viewsets import ModelViewSet
from .models import Missions
from .serializers import MissionSerializer


class MissionModelView(ModelViewSet):

    queryset = Missions.objects.all()
    serializer_class = MissionSerializer

