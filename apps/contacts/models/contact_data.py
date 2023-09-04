from django.db import models
from .contact import Contact
from .contact_data_type import ContactDataType


class ContactData(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    data_type = models.ForeignKey(ContactDataType, on_delete=models.CASCADE)
    value = models.CharField(max_length=100)
