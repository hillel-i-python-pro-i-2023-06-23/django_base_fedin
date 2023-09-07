from django.forms import formset_factory
from django.shortcuts import render, redirect
from apps.contacts.models import Contact, ContactData
from apps.contacts.forms import ContactForm, ContactDataForm


def contact_list_view(request):
    contacts = Contact.objects.all()
    contact_data = ContactData.objects.all()

    info_message = "We got something, but you have no enough permissions to see("
    login_prompt = "Please, log in first"

    return render(
        request=request,
        template_name='contact_list.html',
        context={'contacts': contacts,
                 'contact_data': contact_data,
                 'info_message': info_message,
                 'login_prompt': login_prompt,
                 }
    )


def create_contact_view(request):

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        contact_data_form_set = formset_factory(ContactDataForm, extra=3)

        if 'cancel' in request.POST:
            return redirect('contacts:contact_list')
        else:
            if contact_form.is_valid():
                contact_form.save()
            # contact_form = ContactForm()
            #     return redirect('contacts:contact_list')

        contact_data_formset = contact_data_form_set(request.POST)
    #
    #     # if contact_form.is_valid() and contact_data_formset.is_valid():
    #     contact = contact_form.save()
    #     for form in contact_data_formset:
    #         if form.is_valid():
    #             data_type = form.cleaned_data['data_type']
    #             value = form.cleaned_data['value']
    #
    #             if data_type and value:
    #                 contact_data = ContactData.objects.create(contact=contact, data_type=data_type, value=value)
    #                 contact_data.save()
    #
    #         return redirect('contact_list')
    else:

        contact_form = ContactForm()
        contact_data_form_set = formset_factory(ContactDataForm, extra=3)

    return render(
        request=request,
        template_name='create_contact.html',
        context={'contact_form': contact_form, 'contact_data_formset': contact_data_form_set})
