from django.db import models
from django.core.exceptions import ValidationError


class Job(models.Model):
    name = models.CharField(max_length=100, unique=True)

