from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=20, unique=True)

    is_auto_generated = models.BooleanField(
        blank=False,
        default=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        blank=False,
        null=False,
    )

    def __str__(self):
        return f"{self.name}"

    # Get metadata from model (sort by newest record)
    class Meta:
        ordering = ["-modified_at", "name"]
