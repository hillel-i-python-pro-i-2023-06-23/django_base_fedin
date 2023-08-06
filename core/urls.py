from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from apps.basic import views

urlpatterns = [
    path('compare_string/', views.compare_string, name='compare_string'),
]