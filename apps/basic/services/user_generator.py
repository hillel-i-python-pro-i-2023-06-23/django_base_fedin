# For python
from collections.abc import Iterator

# Get app model
from apps.basic.models import CustomUser
from apps.basic.services.faker import fake_user


def generate_user() -> CustomUser:
    return CustomUser(
        username=fake_user.get_login(),
        email=fake_user.get_email(),
        password=fake_user.get_password(),
    )


def generate_users(
    amount: int,
) -> Iterator[CustomUser]:
    for _ in range(amount):
        yield generate_user()
