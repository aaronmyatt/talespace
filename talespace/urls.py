from django.conf.urls import url, include
from django.contrib import admin
from allauth import urls
from rest_auth import urls as rest_urls
from rest_auth.registration import urls as register_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include(rest_urls)),
    url(r'^auth/registration/', include(register_urls)),
]
