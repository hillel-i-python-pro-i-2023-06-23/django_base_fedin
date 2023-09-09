import logging

from django.core.management.base import BaseCommand

from apps.contacts.models import Contact


class Command(BaseCommand):
    help = "Delete contacts"

    def handle(self, *args, **options) -> None:
        # Log handling to terminal
        logger = logging.getLogger("django")

        # Get queryset template
        queryset = Contact.objects.all()

        logger.info(f"Current amount of contacts before: {queryset.count()}")

        queryset_for_delete = queryset
        logger.info("Delete all generated contacts")
        queryset_for_delete = queryset_for_delete.filter(is_auto_generated=True)

        total_deleted, details = queryset_for_delete.delete()
        logger.info(f"Total deleted: {total_deleted}, details: {details}")

        logger.info(f"Current amount of contacts after deletion: {queryset.count()}")
