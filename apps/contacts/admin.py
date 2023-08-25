from django.contrib import admin

from apps.contacts import models


@admin.register(models.Contact)
class CustomContactAdmin(admin.ModelAdmin):
    list_display = ["name", "phone_number", "created_at"]

    list_filter = [
        "name",
        "created_at",
    ]


@admin.register(models.Job)
class CustomJobAdmin(admin.ModelAdmin):
    list_display = ["name"]


