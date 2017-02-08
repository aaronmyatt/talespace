from django.conf.urls import url, include
from django.contrib import admin

from apps.auth.urls import urlpatterns as auth_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include(auth_urls)),
]
