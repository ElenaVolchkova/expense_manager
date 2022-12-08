from rest_framework import serializers
from transaction.models import Transaction


# class TransactionModel:
#     def __ini__(self, date, amount, organisation):
#         self.date = date
#         self.amount = amount
#         self.organisation = organisation

# class TransactionSerializer(serializers.Serializer):
#     date = serializers.DateTimeField()
#     amount = serializers.DecimalField(max_digits=20, decimal_places=6)
#     organisation = serializers.CharField(max_length=255)
#     description = serializers.CharField()
#     category_id = serializers.IntegerField()


    # class TransactionModel:
    #     def __ini__(self, date, amount, organisation):
    #         self.date = date
    #         self.amount = amount
    #         self.organisation = organisation

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        # fields = ('date', 'amount', 'description', 'organisation')
        fields = "__all__"
    #
    # date = serializers.DateTimeField()
    # amount = serializers.DecimalField(max_digits=20, decimal_places=6)
    # organisation = serializers.CharField(max_length=255)
    # description = serializers.CharField()
    # category_id = serializers.IntegerField()
    #
    # def create(self, validated_data):
    #     return Transaction.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.date = validated_data.get("date", instance.date)
    #     instance.amount = validated_data.get("amount", instance.amount)
    #     instance.organisation = validated_data.get("organisation", instance.organisation)
    #     instance.description = validated_data.get("description", instance.description)
    #     instance.category_id = validated_data.get("category_id", instance.category_id)
    #     instance.save()
    #     return instance

    # class Meta:
    #     model = Transaction
    #     fields = ('date', 'amount', 'category_id', 'organisation')
# def create(self, validated_data):
#     return Transaction.objects.create(**validated_data)
#
# def update(self, instance, validated_data):
#     instance.date = validated_data.get("date", instance.date)
#     instance.amount = validated_data.get("amount", instance.amount)
#     instance.organisation = validated_data.get("organisation", instance.organisation)
#     instance.description = validated_data.get("description", instance.description)
#     instance.category_id = validated_data.get("category_id", instance.category_id)
#     instance.save()
#     return instance

