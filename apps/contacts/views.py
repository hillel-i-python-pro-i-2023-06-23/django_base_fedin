from django.shortcuts import render, redirect
from apps.contacts.models.contact import Contact
from apps.contacts.models.contact_data import ContactData
from apps.contacts.forms import ContactForm


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
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect('contacts:contact_list')
    else:
        form = ContactForm()

    return render(request, 'create_contact.html', {'form': form})

