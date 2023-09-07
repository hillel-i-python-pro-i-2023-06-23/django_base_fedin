import logging
from typing import Final

from django.core.management.base import BaseCommand
from django.core.exceptions import FieldError

from apps.basic.management.commands import create_superuser
from apps.basic.services import generate_user
from apps.basic.models import CustomUser


class Command(BaseCommand):
    help = "Generate users"
    MINIMAL_AMOUNT_OF_CONTACTS: Final[int] = 10

    def handle(self, *args, **options) -> None:
        logger = logging.getLogger("django")
        current_amount_of_users = CustomUser.objects.count()

        amount = self.MINIMAL_AMOUNT_OF_CONTACTS - current_amount_of_users

        if amount > 0:
            logger.info(f"Current amount of users: {CustomUser.objects.count()} but {amount} needed")

            try:
                for _ in range(amount):
                    user = generate_user()
                    user.save()

                logger.info("{new_user_count} users created")

            except FieldError:
                logger.error("Queried object doesn't exist in database.")

        else:
            logger.info("Current amount of users is enough.")

        is_superuser = CustomUser.objects.filter(username="admin").exists()
        if is_superuser:
            logger.info("Superuser already exists. No superuser created.")
            pass
        else:
            new_super_user = create_superuser.Command()
            new_super_user.handle(username="admin", password="admin123", email="admin@gmail.com")

            logger.info("Superuser created")

        logger.info(f"Final amount of users: {CustomUser.objects.count()}")
