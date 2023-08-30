from django.db import models
from apps.contacts.models.contact import Contact
from apps.contacts.models.contact_data_type import ContactDataType


class ContactData(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    data_type = models.ForeignKey(ContactDataType, on_delete=models.CASCADE)
    value = models.CharField(max_length=100)
