from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status

from messages_api.utils import get_test_data
from messages_api.test_container import TestContainer


test_container = TestContainer()


class UserCreationTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user1_data = get_test_data('users.json')['users']['user1']
        cls.first_name = cls.user1_data['first_name']
        cls.username = cls.user1_data['username']
        cls.password = cls.user1_data['password']

    def test_create_user(self):
        c = APIClient()
        data = {
            'first_name': self.first_name,
            'username': self.username,
            'password': self.password,
            'password2': self.password
        }
        c.post(reverse_lazy('sign-up'), data)
        user = get_user_model().objects.get(first_name=self.first_name)
        assert user.username == self.username

    def test_wrong_password(self):
        c = APIClient()
        data = {
            'first_name': self.first_name,
            'username': self.username,
            'password': self.password,
            'password2': f'{self.password}%'
        }
        response = c.post(reverse_lazy('sign-up'), data)
        self.assertFalse(status.is_success(response.status_code))
