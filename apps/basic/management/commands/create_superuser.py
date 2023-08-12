import logging

from django.contrib.auth.management.commands import createsuperuser

from apps.basic.models import CustomUser
from apps.basic.services import generate_users


class Command(createsuperuser.Command):
    help = "Create a superuser"

    def add_arguments(self, parser) -> None:
        parser.add_argument(
            "--amount",
            type=int,
            default=1,
            help="Number of superusers to generate",
        )

    def handle(self, *args, **options):
        amount: int = options["amount"]

        password = 'admin123'
        username = 'admin'
        is_staff = True
        is_superuser = True
        email = ''

        # Log handling to terminal
        logger = logging.getLogger("django")

        # Get queryset template
        logger.info(f"Current amount of superusers before: {amount}")

        for user in generate_users(amount=amount):
            user.is_auto_generated = True
            user.password = password
            user.username = username
            user.is_staff = is_staff
            user.is_superuser = is_superuser
            user.email = email

            user.save()

        logger.info(f"Current amount of superusers after: {amount}")


