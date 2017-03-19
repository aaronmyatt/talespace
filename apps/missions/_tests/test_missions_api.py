from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient

from ..models import Missions


class TestMissionApi(TestCase):
    fixtures = ['users.json', 'missions.json']

    def setUp(self):
        login_details = {
            'email': 'test-admin@user.com',
            'password': '1234qwer'
        }
        self.client = APIClient()
        self.client.login(**login_details)

    def test_gets_a_list_missions(self):
        response = self.client.get('/mission/')
        self.assertEqual(len(response.data), 2)

    def test_get_details_returns_one_object(self):
        mission = Missions.objects.first()
        response = self.client.get('/mission/{}/'.format(str(mission.id)))
        self.assertEqual(response.data['name'], mission.name)

    def test_post_creates_new_record(self):
        url = '/mission/'
        response = self.client.post(url, data={'name': 'BetterMission',
                                          'description': 'ANewMission'})
        self.assertEqual(Missions.objects.count(), 3)

    def test_put_updates_existing_record(self):
        url = '/mission/1/'
        response = self.client.put(url, data={'name': 'BetterMission'})
        mission = Missions.objects.get(id=1)
        self.assertEqual(mission.name, 'BetterMission')

    def test_delete_removes_one(self):
        response = self.client.delete('/mission/1/')
        self.assertEqual(Missions.objects.count(), 1)

    def test_get_nested_skills_returns_missions_skills(self):
        response = self.client.get('/mission/1/required_skills/')
        self.assertEqual(len(response.data), 1)
