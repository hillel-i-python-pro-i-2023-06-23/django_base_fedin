from django.contrib import admin

from apps.contacts.models import Contact


class CustomContactAdmin(admin.ModelAdmin):
    list_display = ["name", "phone_number", "created_at"]

    list_filter = [
        "name",
        "created_at",
    ]


# Register my models here.
admin.site.register(Contact, CustomContactAdmin)
