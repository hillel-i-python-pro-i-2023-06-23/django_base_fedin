from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render
from datetime import datetime

from .forms import CustomUserCreationForm

from apps.basic.models import CustomUser


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


# View to About Us page
def about_view(request):
    return render(request=request, template_name="about.html", context={"greeting_text": "Welcome to our website!", "now": datetime.now(), "user_amount": CustomUser.objects.all().count()})
