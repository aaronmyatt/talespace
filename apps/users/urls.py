from django.conf.urls import url, include
from rest_auth import urls as rest_urls
from rest_auth.registration import urls as register_urls
from rest_framework.routers import DefaultRouter

from .views import CustomUserDetailsView, UserSkillsView

router = DefaultRouter()
router.register('user_skills', UserSkillsView)

urlpatterns = [
    url(r'^user/$', CustomUserDetailsView.as_view(), name='rest_user_details'),
    url(r'', include(rest_urls)),
    url(r'^registration/', include(register_urls)),
]
urlpatterns += router.urls
