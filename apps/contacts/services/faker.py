from faker import Faker


class FakeContact:
    def __init__(self):
        self.faker = Faker()

    def get_name(self):
        return self.faker.unique.first_name()

    def get_phone(self):
        phone_number = self.faker.phone_number()
        digits = "".join(filter(str.isdigit, phone_number))
        custom_phone_number = "+" + digits

        return custom_phone_number

    def get_domain(self):
        return self.faker.unique.domain_name()

    def get_email(self, name):
        email_prefix = name
        domain = self.get_domain()

        return f"{email_prefix}@{domain}"


fake_contact = FakeContact()
