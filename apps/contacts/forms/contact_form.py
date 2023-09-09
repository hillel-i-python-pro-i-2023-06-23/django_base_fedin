import re

from django import forms
from apps.contacts.models import Contact


def has_non_letters(input_string):
    non_letter_pattern = re.compile(r"[^A-Za-z]")
    match = non_letter_pattern.search(input_string)

    return match is not None


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=10)

    def clean_name(self):
        data = self.cleaned_data.get("name")

        if has_non_letters(data):
            raise forms.ValidationError("Entered value has non letters!")

        return data

    class Meta:
        model = Contact
        fields = ["name"]
