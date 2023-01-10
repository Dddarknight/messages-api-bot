from django.contrib import admin
from messages_api.users_messages.models import TgToken, Message


class TgTokenAdmin(admin.ModelAdmin):
    list_display = ('tg_token', 'chat_id', 'user')


class MessageAdmin(admin.ModelAdmin):
    list_display = ('text', 'created_at', 'user')


admin.site.register(TgToken, TgTokenAdmin)
admin.site.register(Message, MessageAdmin)
