from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from apps.basic import models


# Create admin model from user model
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = models.CustomUser

    list_display = ["username", "email", "password", "is_superuser", "is_staff", "state"]

    list_filter = [
        "state",
        "is_superuser",
        "is_staff",
    ]


# Register admin model
admin.site.register(models.CustomUser, CustomUserAdmin)
