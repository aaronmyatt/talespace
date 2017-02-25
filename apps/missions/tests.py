import json
from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
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

    def test_post_updates_existing_record(self):
        client = APIClient()
        response = client.post('/mission/1/', data=json.dumps({'name':'BetterMission'}))
        mission = Missions.objects.first()
        self.assertEqual(mission.name, 'BetterMission')

    def test_delete_removes_one(self):
        client = APIClient()
        response = client.delete('/mission/1/')
        self.assertEqual(Missions.objects.count(), 0)