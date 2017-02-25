from django.conf.urls import url, include
from django.contrib import admin

from apps.users.urls import urlpatterns as user_urls
from apps.missions.urls import urlpatterns as mission_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include(user_urls))
]

urlpatterns += mission_urls