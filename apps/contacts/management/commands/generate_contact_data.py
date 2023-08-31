import logging

from django.core.management.base import BaseCommand
from apps.contacts.models.contact import Contact
from apps.contacts.models.contact_data import ContactData
from apps.contacts.models.contact_data_type import ContactDataType
from apps.contacts.services.faker import fake_contact


class Command(BaseCommand):
    help = "Create each type of contact data for each contact"

    def handle(self, *args, **options):
        contact_type_names = ["Phone Number", "LinkedIn Account", "Email"]

        contact_types = [ContactDataType.objects.get_or_create(name=name)[0] for name in contact_type_names]

        logger = logging.getLogger("django")

        for contact in Contact.objects.all():
            contact_name = contact.name

            logger.info(f"contact_types: {contact_name}")

            value = None

            for contact_type in contact_types:
                if contact_type.name == "Phone Number":
                    value = fake_contact.get_phone()
                elif contact_type.name == "Email":
                    value = fake_contact.get_email(contact_name)
                elif contact_type.name == "LinkedIn Account":
                    raw_value = contact_name
                    value = raw_value[0].lower() + raw_value[1:]
                ContactData.objects.create(contact=contact, data_type=contact_type, value=value)
