from django.core.management.base import BaseCommand
from apps.contacts.models.contact import Contact
from apps.contacts.models.contact_data import ContactData
from apps.contacts.models.contact_data_type import  ContactDataType


class Command(BaseCommand):
    help = "Create each type of contact data for each contact"

    def handle(self, *args, **options):
        contact_types = ContactDataType.objects.all()

        for contact in Contact.objects.all():
            for contact_type in contact_types:
                value = "smth"
                ContactData.objects.create(contact=contact, data_type=contact_type, value=value)

