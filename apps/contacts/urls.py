from django.urls import path
from . import views

app_name = "contacts"

urlpatterns = [
    path('list/', views.contact_list_view, name='contact_list'),
]
