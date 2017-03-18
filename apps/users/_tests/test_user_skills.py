from django.test import TestCase
from rest_framework.test import APIClient
from ..models import UserSkills, UserDetails

class TestUserSkills(TestCase):

    fixtures = ['users.json', 'user_details.json']

    def setUp(self):
        login_details = {
            'email': 'test-admin@user.com',
            'password': '1234qwer'
        }
        self.client = APIClient()
        self.client.login(**login_details)

    def test_get_returns_current_users_skills(self):
        response = self.client.get('/auth/user_skills/')
        self.assertEqual(len(response.data), 1)

    def test_post_creates_a_new_skill(self):
        skill = {
            'level':5,
            'skill':2
        }
        response = self.client.post('/auth/user_skills/', data=skill)
        user = UserDetails.objects.get(user__email='test-admin@user.com')
        self.assertEqual(user.userskills_set.count(), 2)
