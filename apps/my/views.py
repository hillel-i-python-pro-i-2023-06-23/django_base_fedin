from django.http import HttpResponse


# My Django view
def index(request, name: str, age: int):
    return HttpResponse(f"Hello, {name}! My age {age}")
