import logging
from typing import Final

from django.core.management.base import BaseCommand
from django.core import management
from django.db import IntegrityError

from apps.contacts.models import Contact
from apps.contacts.services import fake_contact


class Command(BaseCommand):
    help = "Generate contacts and contact data"
    MINIMAL_AMOUNT_OF_CONTACTS: Final[int] = 10

    def handle(self, *args, **options) -> None:
        logger = logging.getLogger("django")
        current_amount_of_contacts = Contact.objects.count()

        amount_needed = self.MINIMAL_AMOUNT_OF_CONTACTS - current_amount_of_contacts

        if amount_needed > 0:
            logger.info(f"Current amount of contacts: {current_amount_of_contacts} and {amount_needed} needed")

            for _ in range(amount_needed):
                try:
                    contact = Contact.objects.create(name=fake_contact.get_name(), is_auto_generated=True)
                    contact.save()
                except IntegrityError:
                    logger.info("A one newly created contact is not unique and has been skipped")

            logger.info(f"Newly created contact amount: {amount_needed}")

        else:
            logger.info("Current amount of data is enough.")

        newly_created_contact_data = 0
        for contact in Contact.objects.all():
            has_contact_data = Contact.objects.filter(contactdata__contact_id=contact.id).exists()
            if not has_contact_data:
                management.call_command("generate_contact_data", id=contact.id)
                newly_created_contact_data += 1

        logger.info(f"Newly created contact data amount: {newly_created_contact_data}")
