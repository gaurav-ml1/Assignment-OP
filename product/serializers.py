from rest_framework import serializers
from product.models import Category, SubCategory, Product


class CategorySerializer(serializers.ModelSerializer):
    """
    Serialize category objects.
    """

    class Meta:
        model = Category
        fields = "__all__"


class SubCategorySerializer(serializers.ModelSerializer):
    """
    Serialize sub-category objects.
    """

    class Meta:
        model = SubCategory
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    """
    Serialize product objects.
    """

    class Meta:
        model = Product
        fields = "__all__"
        depth = 2

