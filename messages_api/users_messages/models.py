from django.db import models
from django.contrib.auth import get_user_model


class TgToken(models.Model):
    tg_token = models.CharField(max_length=150)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    chat_id = models.CharField(blank=True, null=True, max_length=15)


class Message(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
