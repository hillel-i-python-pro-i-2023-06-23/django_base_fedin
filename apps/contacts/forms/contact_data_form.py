from django import forms
from apps.contacts.models import ContactDataType


class ContactDataForm(forms.Form):
    data_type = forms.ModelChoiceField(queryset=ContactDataType.objects.all())
    value = forms.CharField(max_length=100)

    class Meta:
        model = ContactDataType
        fields = ["data_type", "value"]
