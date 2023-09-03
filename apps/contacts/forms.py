from django import forms
from apps.contacts.models.contact import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=10)

    class Meta:
        model = Contact  # Specify the model class here
        fields = '__all__'
