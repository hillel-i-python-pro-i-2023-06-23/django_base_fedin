import logging

from django.contrib.auth.management.commands import createsuperuser

from apps.basic.services import generate_user


class Command(createsuperuser.Command):
    help = "Create a superuser"

    def add_arguments(self, parser) -> None:
        parser.add_argument(
            "--password",
            type=str,
            default="admin123",
            help="Password of superuser",
        )
        parser.add_argument(
            "--username",
            type=str,
            default="admin",
            help="Name of superuser",
        )
        parser.add_argument(
            "--email",
            type=str,
            default="admin@gmail.com",
            help="Email of superuser",
        )

    def handle(self, *args, **options):
        password: str = options["password"]
        username: str = options["username"]
        email: str = options["email"]

        is_staff = True
        is_superuser = True

        # Log handling to terminal
        logger = logging.getLogger("django")

        user = generate_user()
        user.is_auto_generated = True
        user.set_password(password)
        user.username = username
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.email = email

        user.save()

        logger.info(f"Superuser {username} created with password {password} and email {email}")
