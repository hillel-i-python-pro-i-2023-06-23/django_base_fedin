from apps.contacts.models import ContactDataType, ContactData

contact_data_type_amount = ContactDataType.objects.count()


def contact_data_type_count(data_id: int) -> int:
    contact_data_count = ContactData.objects.filter(data_type_id=data_id).count()

    return contact_data_count


def contact_data_usage() -> list[str]:
    data_type_queryset = ContactDataType.objects.all()
    data_type_dict = {obj.id: obj.name for obj in data_type_queryset}
    usage_list = []

    for key in data_type_dict.keys():
        name = data_type_dict.get(key)
        usage = contact_data_type_count(key)
        usage_item = f"{name} - {usage} item(s)"
        usage_list.append(usage_item)

    return usage_list
