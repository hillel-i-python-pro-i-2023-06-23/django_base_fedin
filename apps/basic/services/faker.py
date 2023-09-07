import string

from faker import Faker


class FakeUser:
    def __init__(self):
        self.faker = Faker()
        self.characters = string.ascii_letters + string.digits + "_"
        self.password_characters = string.ascii_letters + string.digits + "!@#$^()"

    def get_login(self):
        return self.faker.lexify(text="?" * 8, letters=self.characters)

    def get_password(self):
        return self.faker.lexify(text="?" * 3, letters=self.characters)

    def get_text(self):
        return self.faker.lexify(text="?" * 3, letters=self.characters)

    def get_domain(self):
        return self.faker.unique.domain_name()

    def get_email(self):
        login = self.get_login()
        text = self.get_text()
        domain = self.get_domain()

        return f"{login}{text}@{domain}"


fake_user = FakeUser()
