from rest_framework import serializers

from owner.models import Owner


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        # fields = ('date', 'amount', 'description', 'organisation')
        fields = "__all__"