from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import AllowAny

from messages_api.users.serializers import SignUpSerializer


class SignUpView(generics.CreateAPIView):
    """
    Creates the user.
    """
    queryset = get_user_model().objects.all()
    permission_classes = [AllowAny]
    serializer_class = SignUpSerializer
