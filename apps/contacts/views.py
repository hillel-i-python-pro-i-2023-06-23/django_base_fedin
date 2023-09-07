from django.forms import formset_factory
from django.shortcuts import render, redirect
from apps.contacts.models import Contact, ContactData, ContactDataType
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
        contact_data_form_set = ContactDataForm(request.POST)
        # contact_data_form_set = formset_factory(ContactDataForm, extra=3)
        # contact_data_formset = contact_data_form_set(request.POST)
        current_contact_name = 'default_name'

        if 'cancel' in request.POST:
            return redirect('contacts:contact_list')
        elif 'save_contact' in request.POST:
            if contact_form.is_valid():
                # current_contact_name = contact_form.cleaned_data['name']
                contact_form.save()

        if contact_data_form_set.is_valid() and 'submit_data' in request.POST:
            data_type = contact_data_form_set.cleaned_data['data_type']
            value = contact_data_form_set.cleaned_data['value']
            contact = Contact.objects.last()
            contact_data = ContactData.objects.create(contact=contact,
                                                  data_type=data_type,
                                                  value=value)
            contact_data.save()

        # for form in contact_data_formset:
        #     contact = Contact.objects.get(name=current_contact_name)
        #     if form.is_valid() and 'submit_data' in request.POST:
        #         data_type = form.cleaned_data['data_type']
        #         value = form.cleaned_data['value']
        #         form.save()

                # if data_type and value:
            # contact_data = ContactData.objects.create(contact=Contact(name=current_contact_name),
            #                                           data_type=data_type,
            #                                           value=value)
            # contact_data.save()

    else:

        contact_form = ContactForm()
        contact_data_form_set = ContactDataForm()
        # contact_data_form_set = formset_factory(ContactDataForm, extra=3)

    return render(
        request=request,
        template_name='create_contact.html',
        context={'contact_form': contact_form, 'contact_data_form_set': contact_data_form_set})
