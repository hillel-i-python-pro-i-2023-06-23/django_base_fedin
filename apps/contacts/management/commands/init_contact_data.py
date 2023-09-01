import logging
from typing import Final

from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist

from apps.contacts.models.contact import Contact
# from apps.contacts.models.contact_data import ContactData
# from apps.contacts.models.contact_data_type import ContactDataType
from apps.contacts.services.faker import fake_contact


class Command(BaseCommand):
    help = "Generate contacts and contact data"
    MINIMAL_AMOUNT_OF_CONTACTS: Final[int] = 10

    def handle(self, *args, **options) -> None:
        logger = logging.getLogger("django")
        current_amount_of_contacts = Contact.objects.count()

        amount = (self.MINIMAL_AMOUNT_OF_CONTACTS - current_amount_of_contacts)

        logger.info(f"Current amount of contacts: {Contact.objects.count()} but {amount} needed")

        if amount > 0:

            try:
                for _ in range(amount):
                    contact = Contact.objects.create(name=fake_contact.get_name(), is_auto_generated=True)
                    contact.save()

            except ObjectDoesNotExist:
                logger.error(f"Queried object doesn't exist in database.")

        else:
            logger.info(f"Current amount of data is enough.")

        logger.info(f"{amount} contacts created")

        logger.info(f"Final amount of contacts: {Contact.objects.count()}")
