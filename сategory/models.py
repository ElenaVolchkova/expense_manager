# from django.conf.global_settings import AUTH_USER_MODEL
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=25, blank=False)
    description = models.TextField(blank=True)
    is_default = models.BooleanField(default=True, blank=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.category_name