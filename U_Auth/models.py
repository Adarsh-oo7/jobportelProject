from django.db import models
from django.contrib.auth.models import AbstractUser,Group
from django.contrib.auth.models import Permission
# Create your models here.


class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        verbose_name="groups",
        blank=True,
        related_name='u_auth_user_set'  # Ensure this is unique
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name="user permissions",
        blank=True,
        related_name='u_auth_user_permissions_set'  # Ensure this is unique
    )

    is_user = models.BooleanField(default=False)