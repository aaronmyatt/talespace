from rest_framework.routers import DefaultRouter
from .views import MissionModelView

router = DefaultRouter()
router.register('mission', MissionModelView)

urlpatterns = router.urls