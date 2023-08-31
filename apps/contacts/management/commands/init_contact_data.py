import logging
from typing import Final

from django.core.management.base import BaseCommand

from apps.contacts.models.contact import Contact
from apps.contacts.models.contact_data import ContactData
from apps.contacts.models.contact_data_type import ContactDataType
from apps.contacts.services.faker import fake_contact


class Command(BaseCommand):
    help = "Generate contacts and contact data"
    MINIMAL_AMOUNT_OF_CONTACTS: Final[int] = 10

    def handle(self, *args, **options) -> None:
        logger = logging.getLogger("django")
        current_amount_of_contacts = Contact.objects.count()

        amount = (self.MINIMAL_AMOUNT_OF_CONTACTS - current_amount_of_contacts)

        if amount > 0:
            logger.info(f"Current amount of contacts: {Contact.objects.count()} but {amount} needed")
            for _ in range(amount):
                contact = Contact.objects.create(name=fake_contact.get_name(),is_auto_generated=1).save()
                # ContactData.objects.create(contact=contact, data_type=ContactDataType.data_type).save()
        else:
            logger.info(f"Current amount of data is enough.")

        logger.info(f"{amount} contacts created")

        # if amount:
        #     logger.info(f"{amount} contact data needed")
        #     for _ in range(amount):
        #         ContactData.objects.create().save()
        # else:
        #     logger.info(f"Current amount of data is enough.")

        logger.info(f"Final amount of contacts with contact data: {Contact.objects.count()}")
