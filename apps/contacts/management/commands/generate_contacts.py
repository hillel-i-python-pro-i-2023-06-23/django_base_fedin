import logging

from django.core.management.base import BaseCommand

from apps.contacts.models import Contact
from apps.contacts.services import generate_contacts


class Command(BaseCommand):
    help = "Generate contacts"

    # Get parser for command args
    def add_arguments(self, parser) -> None:
        # Set argument with default value
        parser.add_argument(
            "--amount",
            type=int,
            default=20,
            help="Number of users to generate",
        )

    def handle(self, *args, **options) -> None:
        amount: int = options["amount"]

        # Log handling to terminal
        logger = logging.getLogger("django")

        # Get queryset template
        queryset = Contact.objects.all()

        logger.info(f"Amount of contacts before: {queryset.count()}")

        for user in generate_contacts(amount=amount):
            user.is_auto_generated = True
            user.save()

        logger.info(f"Amount of contacts after: {queryset.count()}")
