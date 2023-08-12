from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(max_length=20, unique=True, default=None)
    email = models.EmailField(max_length=20, unique=True)
    is_staff = models.BooleanField(default=False)
    password = models.CharField(max_length=20, unique=True, default=None)

    def __str__(self):
        return self.username
