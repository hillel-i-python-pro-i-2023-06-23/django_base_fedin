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
                contact = Contact.objects.create(name=fake_contact.get_name(), is_auto_generated=True)
                contact.save()

                for data_pk in range(3, 6):
                    data_type_instance = ContactDataType.objects.get(pk=data_pk)
                    if data_pk == 3:
                        contact_data = ContactData.objects.create(contact=contact,
                                                                  data_type=data_type_instance,
                                                                  value=fake_contact.get_phone()
                                                                  )
                        contact_data.save()
                    elif data_pk == 4:
                        contact_data = ContactData.objects.create(contact=contact,
                                                                  data_type=data_type_instance,
                                                                  value=contact.name
                                                                  )
                        contact_data.save()
                    else:
                        name = contact.name
                        contact_data = ContactData.objects.create(contact=contact,
                                                                  data_type=data_type_instance,
                                                                  value=fake_contact.get_email(name)
                                                                  )
                        contact_data.save()
        else:
            logger.info("Current amount of data is enough.")

        logger.info(f"{amount} contacts created")

        logger.info(f"Final amount of contacts with contact data: {Contact.objects.count()}")
