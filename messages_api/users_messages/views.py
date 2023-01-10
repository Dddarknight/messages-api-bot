from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import permission_classes

from messages_api.users_messages.bot import send_message_to_bot
from messages_api.users_messages.models import TgToken, Message
from messages_api.users_messages.serializers import (
    TgTokenCreateSerializer,
    TgTokenSerializer,
    MessageCreateSerializer,
    MessageSerializer,
)


class TgTokenCreateView(generics.CreateAPIView):

    queryset = TgToken.objects.all()
    serializer_class = TgTokenCreateSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return TgTokenCreateSerializer
        return TgTokenSerializer

    @permission_classes((IsAuthenticated,))
    def post(self, request, *args, **kwargs):
        """
        Creates an object TgToken, which is related to request.user.
        The field 'chat_id' of the TgToken object remains empty.
        """
        serializer = TgTokenCreateSerializer(data=request.data)
        if serializer.is_valid():
            TgToken.objects.filter(user=request.user).delete()
            TgToken.objects.create(**serializer.data, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes((AllowAny,))
    def put(self, request, *args, **kwargs):
        """
        Updates an object TgToken, which is related to request.user,
        by adding field 'chat_id'.
        """
        serializer = TgTokenSerializer(data=request.data)
        if serializer.is_valid():
            request_token = serializer.data.get('tg_token')
            chat_id = serializer.data.get('chat_id')
            token = get_object_or_404(TgToken, tg_token=request_token)
            token.chat_id = chat_id
            token.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MessagesView(generics.mixins.CreateModelMixin,
                   generics.mixins.ListModelMixin,
                   generics.GenericAPIView):
    queryset = Message.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return MessageCreateSerializer
        return MessageSerializer

    def get(self, request, *args, **kwargs):
        """
        Return a list of messages, related to request.user.
        """
        messages = Message.objects.filter(user=request.user).all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        """
        Creates a new message, related to request.user,
        and sends it to Telegram bot.
        """
        serializer = MessageCreateSerializer(data=request.data)
        if serializer.is_valid():
            Message.objects.create(**serializer.data, user=request.user)
            send_message_to_bot(request)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
