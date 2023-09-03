from django.shortcuts import render
from apps.contacts.models.contact import Contact
from apps.contacts.models.contact_data import ContactData


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


