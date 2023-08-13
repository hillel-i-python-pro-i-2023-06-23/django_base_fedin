# For python
from collections.abc import Iterator

# Get app model
from apps.basic.models import CustomUser
from apps.basic.services.faker import get_user


def generate_user() -> CustomUser:
    concurrent_credentials = get_user()

    return CustomUser(
        username=concurrent_credentials[0],
        email=concurrent_credentials[1],
        password=concurrent_credentials[2]
    )


def generate_users(
    amount: int,
) -> Iterator[CustomUser]:
    for _ in range(amount):
        yield generate_user()
