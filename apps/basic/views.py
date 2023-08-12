from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.shortcuts import render

from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


# View to About Us page
def about_view(request):
    return render(request, "about.html")


# # View to About Us page
# def home_view(request):
#     return render(request, "home.html")
