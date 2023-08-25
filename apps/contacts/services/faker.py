from apps.basic.services.faker import FakeUser


class FakeContact(FakeUser):

    def get_name(self):
        return self.faker.unique.first_name()

    def get_phone(self):
        return self.faker.phone_number()


fake_contact = FakeContact()
