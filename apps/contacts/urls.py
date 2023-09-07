from django.urls import path
from . import views

app_name = "contacts"

urlpatterns = [
    path("list/", views.contact_list_view, name="contact_list"),
    path("create_contact/", views.create_contact_view, name="create_contact"),
    # path("create_contact/", views.create_contact_data_view, name="create_contact_data"),
]
