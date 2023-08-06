from django.urls import path
from . import views

urlpatterns = [path("", views.compare_string, name="compare_strings")]
