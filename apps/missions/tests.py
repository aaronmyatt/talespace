from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient

from .models import Missions


class TestMissionApi(TestCase):

    def setUp(self):
        u = get_user_model()()
        u.username = 'test'
        u.email = 'test@test.com'
        u.save()
        m = Missions()
        m.user = u
        m.name = 'TestMission'
        m.description = 'Super Mission'
        m.save()

    def test_gets_a_list_missions(self):
        client = APIClient()
        response = client.get('/mission/')
        self.assertEqual(len(response.data), 1)

    def test_get_details_returns_one_object(self):
        mission = Missions.objects.first()
        client = APIClient()
        response = client.get('/mission/{}/'.format(str(mission.id)))
        self.assertEqual(response.data['name'], 'TestMission')

    def test_post_creates_new_record(self):
        client = APIClient()
        url = '/mission/'
        response = client.post(url, data={'name': 'BetterMission',
                                          'description': 'ANewMission',
                                          'user': get_user_model().objects.first().id})
        self.assertEqual(Missions.objects.count(), 2)

    def test_put_updates_existing_record(self):
        mission = Missions.objects.first()
        client = APIClient()
        url = '/mission/{}/'.format(str(mission.id))
        response = client.put(url, data={'name': 'BetterMission'})
        self.assertEqual(mission.name, 'BetterMission')

    def test_delete_removes_one(self):
        client = APIClient()
        response = client.delete('/mission/1/')
        self.assertEqual(Missions.objects.count(), 0)