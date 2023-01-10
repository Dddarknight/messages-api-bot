from _pytest.monkeypatch import MonkeyPatch
from django.urls import reverse_lazy
from rest_framework.test import APITestCase
from rest_framework.test import APIClient

from messages_api.test_container import TestContainer
from messages_api.users_messages import views
from messages_api.users_messages.models import TgToken, Message


test_container = TestContainer()


class TokenCreationTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = test_container.create_user('user1')
        cls.tg_token = 'dummy_string'

    def test_create_tg_token(self):
        c = APIClient()
        c.force_authenticate(user=self.user)
        data = {
            'tg_token': self.tg_token,
        }
        c.post(reverse_lazy('tg-token'), data)
        self.assertTrue(
            TgToken.objects.filter(tg_token=self.tg_token).exists())
        self.assertTrue(
            TgToken.objects.get(tg_token=self.tg_token).user == self.user)
        self.assertTrue(
            TgToken.objects.get(tg_token=self.tg_token).chat_id is None)


class TokenUpdateTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = test_container.create_user('user1')
        cls.token = test_container.create_tg_token(cls.user)
        cls.chat_id = '123'

    def test_update_tg_token(self):
        c = APIClient()
        c.force_authenticate(user=self.user)
        data = {
            'tg_token': self.token.tg_token,
            'chat_id': self.chat_id
        }
        c.put(reverse_lazy('tg-token'), data)
        self.token.refresh_from_db()
        self.assertTrue(self.token.user == self.user)
        self.assertTrue(self.token.chat_id == self.chat_id)


class MessageCreationTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = test_container.create_user('user1')
        cls.text = 'dummy_text'
        cls.monkeypatch = MonkeyPatch()

    def fake_function(self, request):
        pass

    def test_create_msg(self):
        c = APIClient()
        c.force_authenticate(user=self.user)
        data = {
            'text': self.text
        }
        self.monkeypatch.setattr(
            views, 'send_message_to_bot', self.fake_function)
        c.post(reverse_lazy('message'), data)
        self.assertTrue(
            Message.objects.filter(text=self.text).exists())
        self.assertTrue(
            Message.objects.get(text=self.text).user == self.user)


class MessagesTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user1 = test_container.create_user('user1')
        cls.user2 = test_container.create_user('user2')
        cls.message1_1 = test_container.create_message(
            'dummy_text1_1', cls.user1)
        cls.message1_2 = test_container.create_message(
            'dummy_text1_2', cls.user1)
        cls.message2_1 = test_container.create_message(
            'dummy_text2_1', cls.user2)
        cls.message2_2 = test_container.create_message(
            'dummy_text2_2', cls.user2)

    def fake_function(self, request):
        pass

    def test_create_msg(self):
        c = APIClient()
        c.force_authenticate(user=self.user1)
        response = c.get(reverse_lazy('message'))
        self.assertContains(response, 'dummy_text1_1')
        self.assertContains(response, 'dummy_text1_2')
        self.assertNotContains(response, 'dummy_text2_1')
        self.assertNotContains(response, 'dummy_text2_2')
