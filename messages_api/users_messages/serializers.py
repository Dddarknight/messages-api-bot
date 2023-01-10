from rest_framework import serializers

from messages_api.users_messages.models import TgToken, Message


class TgTokenCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TgToken
        fields = ('tg_token', )


class TgTokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = TgToken
        fields = ('tg_token', 'chat_id')


class MessageCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('text', )


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ('text', 'created_at')
