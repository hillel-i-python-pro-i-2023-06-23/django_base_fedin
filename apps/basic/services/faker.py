# Get faker
from faker import Faker


# Get contact fields
def get_user():
    current_faker = Faker()

    current_username = current_faker.first_name()
    current_email = current_faker.email()
    current_password = current_faker.password()

    return current_username, current_email, current_password
