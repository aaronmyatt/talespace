from django.conf.urls import url, include
from django.contrib import admin

from apps.missions.urls import urlpatterns as mission_urls
from apps.skills.urls import urlpatterns as skill_urls
from apps.users.urls import urlpatterns as user_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include(user_urls))
]

urlpatterns += mission_urls
urlpatterns += skill_urls
