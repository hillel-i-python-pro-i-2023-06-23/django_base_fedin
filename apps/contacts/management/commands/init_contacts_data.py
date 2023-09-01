from django.core.management.base import BaseCommand

from apps.contacts import models


class Command(BaseCommand):
    def handle(self, *args, **options):
        for color_as_str in ("Black", "White", "Gray"):
            models.Job.objects.get_or_create(name=color_as_str)
