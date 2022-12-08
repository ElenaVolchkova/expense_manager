from django.contrib.auth.models import User
from django.db import models


class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    name = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} {self.balance}"
