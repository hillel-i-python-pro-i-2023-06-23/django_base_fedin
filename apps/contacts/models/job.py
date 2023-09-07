from django.db import models


class Job(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        self.value = self.name.capitalize()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.value

    __repr__ = __str__
