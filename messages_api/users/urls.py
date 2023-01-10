from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from messages_api.users import views

TokenObtainPairView.__doc__ = ("Returns token for the user "
                               "with given credentials. "
                               "To use the token in headers in /docs "
                               "you need to add 'Bearer your-token' "
                               "after clicking Authorize button.")


urlpatterns = [
    path(
        'token/', TokenObtainPairView.as_view(), name='token_obtain_pair'
    ),
    path(
        'token/refresh/', TokenRefreshView.as_view(), name='token_refresh'
    ),
    path('sign-up/', views.SignUpView.as_view(), name='sign-up'),
]
