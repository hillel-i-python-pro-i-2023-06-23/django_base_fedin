# Get faker
from faker import Faker

import string


def get_user():
    current_faker = Faker()

    # Set character sets
    characters = string.ascii_letters + string.digits + "_"
    password_characters = string.ascii_letters + string.digits + "!@#$^()"

    # Set item templates
    login_template = current_faker.lexify(text="?" * 8, letters=characters)
    text_template = current_faker.lexify(text="?" * 3, letters=characters)
    password_template = current_faker.lexify(text="?" * 12, letters=password_characters)

    # Get items
    current_login = login_template
    current_text = text_template
    current_password = password_template

    # Get domain name
    domain_name = current_faker.unique.domain_name()
    current_email = f"{current_login}{current_text}@{domain_name}"

    return current_login, current_email, current_password
