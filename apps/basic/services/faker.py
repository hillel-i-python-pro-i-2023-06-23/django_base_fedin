# Get faker
from faker import Faker


# Get contact fields
def get_user():
    current_faker = Faker()

    current_login = current_faker.login()
    current_email = current_faker.email()

    return current_login, current_email
