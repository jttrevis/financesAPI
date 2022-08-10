from rest_framework import serializers
from category.models import CategoryAPI


class CategoryAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryAPI
        fields = '__all__'
