from django.contrib.auth.models import AbstractUser

# from django.core.validators import RegexValidator
from django.db import models


class CustomUser(AbstractUser):
    # Add custom field
    state = models.CharField(max_length=100, choices=(("good", "Good"), ("bad", "Bad")), default="good")

    def __str__(self):
        return self.username
