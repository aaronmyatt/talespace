from django.conf.urls import url, include
from rest_auth import urls as rest_urls
from rest_auth.registration import urls as register_urls

urlpatterns = [
    url(r'', include(rest_urls)),
    url(r'^registration/', include(register_urls)),
]
