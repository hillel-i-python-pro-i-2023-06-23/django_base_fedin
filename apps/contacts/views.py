from django.shortcuts import render
from apps.contacts.models.contact import Contact


def contact_list_view(request):
    contacts = Contact.objects.all()

    return render(
        request=request,
        template_name='contact_list.html',
        context={'contacts': contacts}
    )


