# For python
from collections.abc import Iterator

# Get app model
from apps.contacts.models.contact import Contact
from apps.contacts.services.faker import fake_contact


def generate_contact() -> Contact:
    return Contact(
        name=fake_contact.get_name(),
        # phone_number=fake_contact.get_phone(),
        # password=fake_contact.get_password(), # :TODO: reserved for birth date
    )


def generate_contacts(
    amount: int,
) -> Iterator[Contact]:
    for _ in range(amount):
        yield generate_contact()
