from django.urls import path

from messages_api.users_messages import views


urlpatterns = [
    path('tg-token/', views.TgTokenCreateView.as_view(), name='tg-token'),
    path('', views.MessagesView.as_view(), name='message'),
]
