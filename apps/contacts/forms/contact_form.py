from django import forms
from apps.contacts.models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=10)

    class Meta:
        model = Contact
        fields = ["name"]
