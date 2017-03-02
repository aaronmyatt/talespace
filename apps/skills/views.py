from rest_framework.viewsets import ModelViewSet

from .models import Skills
from .serializers import SkillSerializer


class SkillModelView(ModelViewSet):
    queryset = Skills.objects.all()
    serializer_class = SkillSerializer
