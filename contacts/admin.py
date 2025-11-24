from django.contrib import admin
from .models import Contact, Group

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "phone")
    search_fields = ("full_name", "email")
    list_filter = ("groups",)

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)
