from .models import UserDetails
from rest_auth.views import UserDetailsView

class CustomUserDetailsView(UserDetailsView):

    def get_object(self):
        user = self.request.user
        return UserDetails.objects.get(user=user)