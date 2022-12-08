from rest_framework import serializers

from сategory.models import Category


class CategorySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Category
        # fields = ('category_name', 'description', 'is_default', 'owner')
        fields = "__all__"


