import logging
from typing import Final

from django.core.management.base import BaseCommand

from apps.contacts.models.contact import Contact
from apps.contacts.services.faker import fake_contact


class Command(BaseCommand):
    help = "Generate contacts and contact data"
    MINIMAL_AMOUNT_OF_CONTACTS: Final[int] = 10

    def handle(self, *args, **options) -> None:
        logger = logging.getLogger("django")
        current_amount_of_contacts = Contact.objects.count()

        if (amount := (self.MINIMAL_AMOUNT_OF_CONTACTS - current_amount_of_contacts)) > 0:
            logger.info(f"Current amount of contacts: {Contact.objects.count()} but {amount} needed")
            for _ in range(amount):
                Contact.objects.create(name=fake_contact.get_name()).save()
        else:
            logger.info(f"Current amount of data is enough.")

        logger.info(f"Final amount of contacts with contact data: {Contact.objects.count()}")
