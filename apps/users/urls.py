from django.conf.urls import url, include
from rest_auth import urls as rest_urls
from rest_auth.registration import urls as register_urls
from .views import CustomUserDetailsView

urlpatterns = [
    url(r'^user/$', CustomUserDetailsView.as_view(), name='rest_user_details'),
    url(r'', include(rest_urls)),
    url(r'^registration/', include(register_urls)),
]
