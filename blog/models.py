from django.db import models
from django.utils import timezone

#from django.contrib.auth.models import User
from accounts.models import CustomUser

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name="")
    sub_title = models.CharField(max_length=100, null=False, blank=False, verbose_name="")
    body = models.TextField(max_length=500, null=False, blank=False, verbose_name="")
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    #image = models.ImageField(upload_to='blog_images', null=True, blank=True)
    create_date = models.DateField(default=timezone.now, editable=False)

    def __str__(self) -> str:
        return f' Title: {self.title}'