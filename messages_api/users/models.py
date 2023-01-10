from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(
        blank=False, max_length=150, verbose_name='first name')
    email = models.EmailField(
        blank=True, max_length=150, verbose_name='email address')

    def __str__(self):
        return f'{self.username}'
