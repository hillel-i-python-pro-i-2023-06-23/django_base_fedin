import logging

from django.core.management.base import BaseCommand

from apps.contacts.models import Contact


class Command(BaseCommand):
    help = "Delete contacts"

    # Get parser for command args
    def add_arguments(self, parser) -> None:
        # Set argument with default value
        parser.add_argument(
            "--is_only_auto_generated",
            help="Number of contacts to generate",
            action="store_true",
        )

    def handle(self, *args, **options) -> None:
        is_only_auto_generated: bool = options["is_only_auto_generated"]

        # Log handling to terminal
        logger = logging.getLogger("django")

        # Get queryset template
        queryset = Contact.objects.all()

        logger.info(f"Current amount of contacts before: {queryset.count()}")

        queryset_for_delete = queryset
        if is_only_auto_generated:
            logger.info("Delete only auto generated contacts")
            queryset_for_delete = queryset_for_delete.filter(is_auto_generated=True)

        total_deleted, details = queryset_for_delete.delete()
        logger.info(f"Total deleted: {total_deleted}, details: {details}")

        logger.info(f"Current amount of contacts after deletion: {queryset.count()}")
