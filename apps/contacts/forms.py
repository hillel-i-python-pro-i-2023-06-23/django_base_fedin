from django import forms
from apps.contacts.models.contact import Contact
from apps.contacts.models.contact_data_type import ContactDataType


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=10)

    data_type = forms.ModelChoiceField(queryset=ContactDataType.objects.all())
    value = forms.CharField(max_length=100)

    class Meta:
        model = Contact
        fields = ['name', 'data_type', 'value']
