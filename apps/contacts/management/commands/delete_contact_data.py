import logging

from django.core.management.base import BaseCommand
from apps.contacts.models import ContactData


class Command(BaseCommand):
    help = "Delete all contact data from the database"

    def handle(self, *args, **options):
        logger = logging.getLogger("django")

        queryset = ContactData.objects.all()
        logger.info(f"Current amount of contacts before: {queryset.count()}")

        total_deleted, details = ContactData.objects.all().delete()
        logger.info(f"Total deleted: {total_deleted}")
