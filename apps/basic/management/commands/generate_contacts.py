import logging

from django.core.management.base import BaseCommand

from apps.basic.models import CustomUser
from apps.basic.services import generate_users


class Command(BaseCommand):
    help = "Generate users"

    # Get parser for command args
    def add_arguments(self, parser) -> None:
        # Set argument with default value
        parser.add_argument(
            "--amount",
            type=int,
            help="Number of contacts to generate",
            default=20,
        )

    def handle(self, *args, **options) -> None:
        amount: int = options["amount"]

        # Log handling to terminal
        logger = logging.getLogger("django")

        # Get queryset template
        queryset = CustomUser.objects.all()

        logger.info(f"Current amount of animals before: {queryset.count()}")

        for contact in generate_users(amount=amount):
            contact.is_auto_generated = True
            contact.save()

        logger.info(f"Current amount of animals after: {queryset.count()}")
