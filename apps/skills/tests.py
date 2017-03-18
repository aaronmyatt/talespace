from django.test import TestCase
from rest_framework.test import APIClient

from .models import Skills


class TestSkillApi(TestCase):
    def setUp(self):
        m = Skills()
        m.name = 'TestSkill'
        m.description = 'A testy skill.'
        m.save()

    def test_gets_a_list_missions(self):
        client = APIClient()
        response = client.get('/skill/')
        self.assertEqual(len(response.data), 1)

    def test_get_details_returns_one_object(self):
        skill = Skills.objects.first()
        client = APIClient()
        response = client.get('/skill/{}/'.format(str(skill.id)))
        self.assertEqual(response.data['name'], 'TestSkill')

    def test_post_creates_new_record(self):
        client = APIClient()
        url = '/skill/'
        response = client.post(url, data={'name': 'BetterSkill'})
        self.assertEqual(Skills.objects.count(), 2)

    def test_put_updates_existing_record(self):
        skill = Skills.objects.first()
        client = APIClient()
        url = '/skill/{}/'.format(str(skill.id))
        response = client.put(url, data={'name': 'BetterSkill'})
        skill = Skills.objects.first()
        self.assertEqual(skill.name, 'BetterSkill')

    def test_delete_removes_one(self):
        client = APIClient()
        response = client.delete('/skill/1/')
        self.assertEqual(Skills.objects.count(), 0)
