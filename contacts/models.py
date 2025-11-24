from django.db import models

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    # ManyToMany: contact can be in many groups
    groups = models.ManyToManyField(
        Group,
        related_name="contacts",
    )

    full_name = models.CharField(max_length=150, blank=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    phone = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
