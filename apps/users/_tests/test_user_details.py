from django.test import TestCase
from rest_framework.test import APIClient
from ..models import UserDetails


class TestAuthUserApi(TestCase):
    fixtures = ['users.json', 'user_details.json']

    def setUp(self):
        login_details = {
            'email': 'test-admin@user.com',
            'password': '1234qwer'
        }
        self.client = APIClient()
        self.client.login(**login_details)

    def test_get_details_returns_one_object(self):
        response = self.client.get('/auth/user/')
        self.assertEqual(response.data['user']['username'], 'test-admin')

    def test_put_updates_user_details_model(self):
        data = {"school": "educational"}
        response = self.client.put('/auth/user/', data=data)
        user = UserDetails.objects.first()
        self.assertEqual(user.school, 'educational')
