from django.urls import path
from . import views

urlpatterns = [
    # Contacts routes
    path("contacts/", views.contact_list, name="contact_list"),
    path("contacts/create/", views.contact_create, name="contact_create"),
    path("contacts/<int:contact_id>/edit/", views.contact_update, name="contact_update"),
    path("contacts/<int:contact_id>/delete/", views.contact_delete, name="contact_delete"),

    # Groups routes
    path("groups/", views.group_list, name="group_list"),
    path("groups/create/", views.group_create, name="group_create"),
    path("groups/<int:group_id>/edit/", views.group_update, name="group_update"),
    path("groups/<int:group_id>/delete/", views.group_delete, name="group_delete"),
]
