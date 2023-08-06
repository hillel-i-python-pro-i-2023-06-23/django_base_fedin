from django.db import models


class DataStored(models.Model):
    stored_string = models.CharField(max_length=20)
