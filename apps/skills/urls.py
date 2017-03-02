from rest_framework.routers import DefaultRouter

from .views import SkillModelView

router = DefaultRouter()
router.register('skill', SkillModelView)

urlpatterns = router.urls
