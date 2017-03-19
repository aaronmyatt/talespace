from rest_framework.routers import DefaultRouter
from .views import MissionModelView, MissionSkillsView

router = DefaultRouter()
router.register('mission', MissionModelView)
router.register('mission_skills', MissionSkillsView)

urlpatterns = router.urls
