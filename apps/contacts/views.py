from django.shortcuts import render
from apps.contacts.models.contact import Contact
from apps.contacts.models.contact_data import ContactData


# def contact_home_view(request):
#     contacts = Contact.objects.all()
#
#     return render(
#         request=request,
#         template_name='home.html',
#         context={'contacts': contacts}
#     )


def contact_list_view(request):
    contacts = Contact.objects.all()
    contac_tdata = ContactData.objects.all()

    return render(
        request=request,
        template_name='contact_list.html',
        context={'contacts': contacts,
                 'contact_data': contac_tdata,
                 }
    )


