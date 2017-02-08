from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient


class TestLoginUrl(TestCase):
    def setUp(self):
        user = get_user_model().objects.create(username='test')
        user.set_password('test')
        user.save()

    def test_login(self):
        login_details = {
            'username': 'test',
            'password': 'test'
        }
        res = APIClient().post('/auth/login/', login_details, format='json')
        self.assertEqual(res.status_code, 200)


class TestRegisterUrl(TestCase):
    def setUp(self):
        pass

    def test_registration(self):
        register_details = {
            'first_name': 'test',
            'last_name': 'test',
            'username': 'test',
            'password1': '12345qwert',
            'password2': '12345qwert',
            'email': 'test@test.com'
        }
        res = APIClient().post('/auth/registration/', register_details, format='json')
        self.assertEqual(res.status_code, 201)
