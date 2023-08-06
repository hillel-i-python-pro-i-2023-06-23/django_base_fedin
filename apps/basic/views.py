from django.shortcuts import render

from .models import DataStored


def compare_string(request):
    input_string = request.POST.get("input_string")
    stored_data = DataStored.objects.first()

    if request.method == "POST":
        if input_string == stored_data:
            message = "String match!"
        else:
            message = "String doesn't match!"

        return render(request, "game/result.html", {"message": message})

    return render(request, "game/forms.html")
