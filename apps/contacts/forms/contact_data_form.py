import re

from django import forms
from apps.contacts.models import ContactDataType
from apps.contacts.forms import has_non_letters


def starts_with_plus_and_numbers(input_string):
    pattern = re.compile(r"^\+\d+$")
    match = pattern.match(input_string)

    return match is not None


def has_characters_other_than_sequence(input_string):
    pattern = re.compile(r"[^A-Za-z@]")
    match = pattern.search(input_string)

    return match is not None


class ContactDataForm(forms.Form):
    data_type = forms.ModelChoiceField(queryset=ContactDataType.objects.all())
    value = forms.CharField(max_length=100)

    def cleaned_value(self, data_type):
        data = self.cleaned_data.get("value")

        if data_type == data_type.objects.get(name="Phone Number"):
            if starts_with_plus_and_numbers(data):
                raise forms.ValidationError("Entered value should be in format [+809835...]!")
        elif data_type == data_type.objects.get(name="Email"):
            if has_characters_other_than_sequence(data):
                raise forms.ValidationError("Entered value should be in format [name@damain]!")
        else:
            if has_non_letters(data):
                raise forms.ValidationError("Entered value should be name-like!")

        return data

    class Meta:
        model = ContactDataType
        fields = ["data_type", "value"]
