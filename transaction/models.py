from django.db import models
from owner.models import Owner
from сategory.models import Category


class Transaction(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, blank=True)
    date = models.DateTimeField(auto_now_add=False)
    amount = models.DecimalField(max_digits=20, decimal_places=6)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    organisation = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.date}, {self.amount}"


    # def update_balance(self, request, *args, **kwargs):
    #     print(request, *args, **kwargs)
    #     if request.method == "POST":
    #         # pk = kwargs.get('pk', None)
    #         owner_id = kwargs.get('owner_id', None)
    #         owner = Owner.objects.get(pk=owner_id)
    #         transaction_amount = kwargs.get('amount', None)
    #         # update_balance = float(self.balance) - float(transaction)
    #         owner.balance -= float(transaction_amount)
    #         owner.save(update_fields=["balance"])
