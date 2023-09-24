from django.db.models import Count

from apps.contacts.models import Contact, ContactDataType, ContactData


def contact_data_type_amount():
    return ContactDataType.objects.count()


def contact_data_type_count(data_id: int) -> int:
    contact_data_count = ContactData.objects.filter(data_type_id=data_id).count()

    return contact_data_count


# def contact_data_usage() -> list[str]:
#     data_type_queryset = ContactDataType.objects.all()
#     data_type_dict = {obj.id: obj.name for obj in data_type_queryset}
#     usage_list = []
#
#     for key in data_type_dict.keys():
#         name = data_type_dict.get(key)
#         usage = contact_data_type_count(key)
#         usage_item = f"{name} - {usage} item(s)"
#         usage_list.append(usage_item)
#
#     return usage_list


def contact_data_usage() -> list[str]:
    data_type_queryset = ContactDataType.objects.all()

    return [f"{data_type} - {data_type.id} item(s)" for data_type in data_type_queryset]


# def user_datatype_count():
#     queryset = Contact.objects.annotate(data_count=Count("contactdata"))
#     data_counts = []
#
#     for item in queryset:
#         data_count = item.data_count
#         data_counts.append(f"{item.name} - {data_count}")
#         # data_counts.append(data_count)
#
#     # return queryset[9].data_count
#     return data_counts


def user_datatype_count():
    queryset = Contact.objects.annotate(data_count=Count("contactdata"))

    return [f"{item.name} - {item.data_count}" for item in queryset]
