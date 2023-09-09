from django.urls import path

from .views import SignUpView, about_view

app_name = "basic"

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("about/", about_view, name="about"),
]
