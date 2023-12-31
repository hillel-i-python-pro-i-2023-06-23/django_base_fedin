# Generated by Django 4.2.3 on 2023-08-24 19:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("basic", "0007_customuser_state"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=20, unique=True)),
                ("phone_number", models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number is invalid", regex="^\\+?1?[-().\\dx]{9,20}$")])),
                ("is_auto_generated", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["-modified_at", "name"],
            },
        ),
    ]
