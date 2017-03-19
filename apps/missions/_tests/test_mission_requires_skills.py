from django.test import TestCase
from rest_framework.test import APIClient
from ..models import MissionRequiresSkills, Missions

class TestMissionRequiresSkills(TestCase):

    fixtures = ['users.json', 'missions.json']

    def setUp(self):
        login_details = {
            'email': 'test-admin@user.com',
            'password': '1234qwer'
        }
        self.client = APIClient()
        self.client.login(**login_details)

    def test_get_returns_all_skills(self):
        response = self.client.get('/mission_skills/')
        self.assertEqual(len(response.data), 2)

    def test_get_returns_one_skill(self):
        response = self.client.get('/mission_skills/1/')
        mrs = MissionRequiresSkills.objects.first()
        self.assertEqual(response.data['mission'], mrs.id)
