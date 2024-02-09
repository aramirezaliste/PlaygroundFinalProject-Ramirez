from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    description = models.TextField(max_length=200, null=True, blank=True, verbose_name="description")
    link = models.CharField(max_length=50, null=True, blank=True, verbose_name="link")
