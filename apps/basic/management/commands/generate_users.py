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
            default=20,
            help="Number of users to generate",
        )

    def handle(self, *args, **options) -> None:
        amount: int = options["amount"]

        # Log handling to terminal
        logger = logging.getLogger("django")

        # Get queryset template
        queryset = CustomUser.objects.all()

        logger.info(f"Amount of users before: {queryset.count()}")

        for user in generate_users(amount=amount):
            user.is_auto_generated = True
            user.set_password(user.password)
            user.save()

        logger.info(f"Amount of users after: {queryset.count()}")
