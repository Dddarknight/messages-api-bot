import os
import requests

from messages_api.users_messages.models import TgToken


API_TOKEN = os.getenv('TG_API_TOKEN')
URL = f'https://api.telegram.org/bot{API_TOKEN}/sendMessage'


def send_message_to_bot(request):
    chat_id = int(TgToken.objects.get(user=request.user).chat_id)
    name = request.user.first_name
    text = f"{name}, я получил от тебя сообщение: \n{request.data.get('text')}"
    requests.post(URL, data={'chat_id': chat_id, 'text': text})
