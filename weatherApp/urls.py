from django.urls import path
from . import views

urlpatterns = [
    path("", views.process_input, name='process_input')
]