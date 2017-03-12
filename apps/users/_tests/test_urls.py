from django.test import TestCase
from rest_framework.test import APIClient

from apps.users.models import UserDetails


class TestLoginUrl(TestCase):
    fixtures = ['users.json']

    def test_login(self):
        login_details = {
            'email': 'test-admin@user.com',
            'password': '1234qwer'
        }
        res = APIClient().post('/auth/login/', login_details, format='json')
        self.assertEqual(res.status_code, 200)


class TestRegisterUrl(TestCase):
    fixtures = ['users.json']
    url = '/auth/registration/'

    def setUp(self):
        self.details = {
            'first_name': 'test',
            'last_name': 'test',
            'username': 'test',
            'password1': '12345qwert',
            'password2': '12345qwert',
            'email': 'test@test.com',
            'user_type': 'v'
        }

    def test_registration(self):
        res = APIClient().post(self.url, self.details, format='json')
        self.assertEqual(res.status_code, 201)

    def test_user_details_model_created_at_registration(self):
        res = APIClient().post(self.url, self.details, format='json')
        self.assertGreater(UserDetails.objects.count(), 0)

    def test_user_type_defaults_to_volunteer(self):
        details = self.details.copy()
        details['user_type'] = ''
        APIClient().post(self.url, details, format='json')
        ud = UserDetails.objects.get(user__username='test')
        self.assertEqual(ud.user_type, 'v')

    def test_sets_user_type_to_mission(self):
        details = self.details.copy()
        details['user_type'] = 'm'
        APIClient().post(self.url, details, format='json')
        ud = UserDetails.objects.get(user__username=details['username'])
        self.assertEqual(ud.user_type, 'm')