from django.test import TestCase

from messages_api.test_container import TestContainer
from messages_api.users_messages.models import TgToken, Message


test_container = TestContainer()


class TgTokenModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = test_container.create_user('user1')
        cls.tg_token = test_container.create_tg_token(cls.user)

    def test_token_creation(self):
        self.assertTrue(isinstance(self.tg_token, TgToken))
        self.assertEqual(self.tg_token.tg_token, 'dummy_string')
        self.assertEqual(self.tg_token.user, self.user)
        self.assertEqual(self.tg_token.chat_id, None)


class MessageModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = test_container.create_user('user1')
        cls.message = test_container.create_message(
            'dummy_text', cls.user)

    def test_msg_creation(self):
        self.assertTrue(isinstance(self.message, Message))
        self.assertEqual(self.message.text, 'dummy_text')
        self.assertEqual(self.message.user, self.user)
