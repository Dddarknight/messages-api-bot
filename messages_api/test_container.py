from django.test import TestCase

from django.contrib.auth import get_user_model
from messages_api.utils import get_test_data
from messages_api.users_messages.models import TgToken, Message


class TestContainer(TestCase):
    test_data_users = get_test_data('users.json')

    def create_user(self, user):
        return get_user_model().objects.create(
            first_name=self.test_data_users['users'][user]['first_name'],
            username=self.test_data_users['users'][user]['username'],
            password=self.test_data_users['users'][user]['password'])

    def create_tg_token(self, user):
        return TgToken.objects.create(
            tg_token='dummy_string',
            user=user
        )

    def create_message(self, text, user):
        return Message.objects.create(
            text=text,
            user=user
        )
