# from django.conf.global_settings import AUTH_USER_MODEL
from django.db import models

# Create your models here.
from rest_framework.authtoken.admin import User

from сategory.models import Category


class Transaction(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    date = models.DateTimeField(auto_now_add=False) # время
    amount = models.DecimalField(max_digits=20, decimal_places=6)  # сумму
    description = models.TextField(blank=True) # описание
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True) # категорию
    organisation = models.CharField(max_length=255) # организацию

    def __str__(self):
        return f"{self.date}, {self.amount}"


    # def update_balance(self, request, *args, **kwargs):
    #     if request.method == "POST":
    #         # pk = kwargs.get('pk', None)
    #         owner_id = kwargs.get('owner_id', None)
    #         from owner.models import Owner
    #         owner = Owner.objects.get(user_id=owner_id)
    #         transaction_amount = kwargs.get('amount', None)
    #         # update_balance = float(self.balance) - float(transaction)
    #         owner.balance -= float(transaction_amount)
    #         owner.save(update_fields=["balance"])
