from django.core.management.base import BaseCommand
from apps.contacts.models import Contact, ContactData, ContactDataType
from apps.contacts.services import fake_contact


class Command(BaseCommand):
    help = "Create each type of contact data for each contact"

    def add_arguments(self, parser) -> None:
        parser.add_argument(
            "--id",
            type=int,
            default=10,
            help="Number of contacts to generate",
        )

    def handle(self, *args, **options):
        id_input: int = options["id"]
        contact_type_names = ["Phone Number", "LinkedIn Account", "Email"]

        contact_types = [ContactDataType.objects.get_or_create(name=name)[0] for name in contact_type_names]

        contact_item = Contact.objects.get(id=id_input)
        contact_name = contact_item.name
        value = None

        for contact_type in contact_types:
            if contact_type.name == "Phone Number":
                value = fake_contact.get_phone()
            elif contact_type.name == "Email":
                value = fake_contact.get_email(contact_name)
            elif contact_type.name == "LinkedIn Account":
                raw_value = contact_name
                value = raw_value[0].lower() + raw_value[1:]
            ContactData.objects.create(contact=contact_item, data_type=contact_type, value=value)
