from django.urls import path

# Import view from my app
from apps.my import views

app_name = "my"

# Add routes instead of using decorators in views
urlpatterns = [
    path("<name>/<int:age>/", views.index, name="Index"),
]
