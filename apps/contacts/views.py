from django.shortcuts import render, redirect
from apps.contacts.models import Contact, ContactData
from apps.contacts.forms import ContactForm, ContactDataForm
from apps.contacts.services import contact_data_type_amount, contact_data_usage, user_datatype_count


def contact_list_view(request):
    contacts = Contact.objects.all()
    contact_data = ContactData.objects.all()

    data_type_amount = contact_data_type_amount
    usage = contact_data_usage()
    data_type_count = user_datatype_count()

    info_message = "We got something, but you have no enough permissions to see("
    login_prompt = "Please, log in first"

    return render(
        request=request,
        template_name="contact_list.html",
        context={
            "contacts": contacts,
            "contact_data": contact_data,
            "info_message": info_message,
            "login_prompt": login_prompt,
            "data_type_amount": data_type_amount,
            "usage": usage,
            "data_type_count": data_type_count,
        },
    )


def create_contact_view(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        contact_data_form = ContactDataForm(request.POST)

        if contact_form.is_valid():
            if "save_contact" in request.POST:
                contact_form.save()
            if "cancel" in request.POST:
                return redirect("contacts:contact_list")

        if contact_data_form.is_valid():
            if "submit_data" in request.POST:
                data_type = contact_data_form.cleaned_data["data_type"]
                value = contact_data_form.cleaned_data["value"]
                contact = Contact.objects.latest("id")
                contact_data = ContactData.objects.create(contact=contact, data_type=data_type, value=value)

                contact_data.save()

            if "cancel_data" in request.POST:
                return redirect("contacts:contact_list")

    else:
        contact_form = ContactForm()
        contact_data_form = ContactDataForm()

    return render(request=request, template_name="create_contact.html", context={"contact_form": contact_form, "contact_data_form": contact_data_form})
