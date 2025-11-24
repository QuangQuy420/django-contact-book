from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from .models import Contact, Group
from django.http import HttpResponse


# Contacts
def contact_list(request):
    contacts = Contact.objects.prefetch_related("groups")
    return render(request, "contacts/contact_list.html", {"contacts": contacts})


def contact_create(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        group_id = request.POST.get("group_id")  # from <select name="group_id">

        if not full_name or not email:
            groups = Group.objects.all()
            return render(
                request,
                "contacts/contact_create.html",
                {
                    "groups": groups,
                    "error": "Full name and email are required.",
                },
            )

        with transaction.atomic():
            # Create the contact
            contact = Contact.objects.create(
                full_name=full_name,
                email=email,
                phone=phone,
            )

            # Attach the selected group (ManyToMany)
            if group_id:
                group = Group.objects.filter(id=group_id).first()
                if group:
                    contact.groups.add(group)

        return redirect("contact_list")

    # GET request → show form
    groups = Group.objects.all()
    return render(request, "contacts/contact_create.html", {"groups": groups})


def contact_update(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)

    if request.method == "POST":
        full_name = request.POST.get("full_name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        group_id = request.POST.get("group_id")

        if not full_name or not email:
            groups = Group.objects.all()
            return render(
                request,
                "contacts/contact_update.html",
                {"contact": contact, "groups": groups, "error": "Full name and email are required."},
            )

        with transaction.atomic():
            contact.full_name = full_name
            contact.email = email
            contact.phone = phone
            contact.save()

            # Replace groups with selected group (matching create behavior)
            contact.groups.clear()
            if group_id:
                group = Group.objects.filter(id=group_id).first()
                if group:
                    contact.groups.add(group)

        return redirect("contact_list")

    # GET -> show form prefilled
    groups = Group.objects.all()
    return render(request, "contacts/contact_update.html", {"contact": contact, "groups": groups})


def contact_delete(request, contact_id):
    if request.method != "POST":
        return HttpResponse(status=405)

    contact = get_object_or_404(Contact, id=contact_id)
    contact.delete()
    return redirect("contact_list")


# Groups
def group_list(request):
    groups = Group.objects.prefetch_related("contacts")
    return render(request, "groups/group_list.html", {"groups": groups})


def group_create(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        description = request.POST.get("description", "").strip()

        if not name:
            return render(
                request,
                "groups/group_create.html",
                {"error": "Group name is required."},
            )

        Group.objects.create(
            name=name,
            description=description
        )

        return redirect("group_list")

    return render(request, "groups/group_create.html")


def group_update(request, group_id):
    group = get_object_or_404(Group, id=group_id)

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        description = request.POST.get("description", "").strip()

        if not name:
            return render(
                request,
                "groups/group_update.html",
                {"group": group, "error": "Group name is required."},
            )

        group.name = name
        group.description = description
        group.save()
        return redirect("group_list")

    # GET -> show form prefilled
    return render(request, "groups/group_update.html", {"group": group})


def group_delete(request, group_id):
    if request.method != "POST":
        return HttpResponse(status=405)  # Method not allowed

    group = get_object_or_404(Group, id=group_id)
    group.delete()
    return redirect("group_list")


# def batch_deactivate_contacts(request):
#     """
#     Example: batch mark contacts as inactive atomically.
#     If error occurs in middle → rollback all changes.
#     """
#     with transaction.atomic():
#         sid = transaction.savepoint()

#         try:
#             # For demo: get first group
#             group = Group.objects.first()
#             if not group:
#                 return HttpResponse("No group found")

#             contacts = Contact.objects.filter(groups=group)

#             for c in contacts:
#                 c.phone = ""  # mock update
#                 c.save()

#             # simulate an error
#             # raise ValueError("Something went wrong!")

#             transaction.savepoint_commit(sid)

#         except Exception as exc:
#             transaction.savepoint_rollback(sid)
#             return HttpResponse(f"Rolled back due to error: {exc}")

#     return HttpResponse("Batch update completed successfully")