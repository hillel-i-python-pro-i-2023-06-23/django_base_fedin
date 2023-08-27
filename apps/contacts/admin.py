from django.contrib import admin
from apps.contacts.models.contact import Contact


@admin.register(Contact)
class CustomContactAdmin(admin.ModelAdmin):
    list_display = ["name", "phone_number", "created_at", "modified_at", "is_auto_generated"]

    list_filter = [
        "name",
        "created_at",
    ]

