from django.urls import path
from . import views

urlpatterns = [
    path(
        "fernand/",
        views.student_form,
        name="dynamic_form",
    ),
]
