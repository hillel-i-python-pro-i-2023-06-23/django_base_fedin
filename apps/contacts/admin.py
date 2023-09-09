from django.contrib import admin
from apps.contacts.models.contact import Contact
from apps.contacts.models.contact_data import ContactData
from apps.contacts.models.contact_data_type import ContactDataType


class ContactDataInline(admin.TabularInline):
    model = ContactData
    readonly_fields = ("id",)
    extra = 1


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "modified_at", "is_auto_generated"]

    inlines = [ContactDataInline]

    list_filter = [
        "name",
        "created_at",
    ]


@admin.register(ContactData)
class ContactDataAdmin(admin.ModelAdmin):
    list_display = [
        "contact",
        "data_type",
        "value",
    ]

    list_filter = [
        "contact",
    ]


@admin.register(ContactDataType)
class ContactDataTypeAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]

    list_filter = [
        "name",
    ]
