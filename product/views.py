from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.response import Response

from product.models import Category, SubCategory, Product
from product.serializers import CategorySerializer, SubCategorySerializer, ProductSerializer


class CategoryListAPIView(ListAPIView):
    """
    listed categories.
    """
    queryset = Category.objects.filter(is_active=True).order_by('name')
    serializer_class = CategorySerializer


class SubCategoryListAPIView(ListAPIView):
    """
    listed categories.
    """
    queryset = SubCategory.objects.filter(is_active=True).order_by('name')
    serializer_class = SubCategorySerializer


class ProductListCreateAPIView(ListCreateAPIView):
    """
    Product create and listed View .
    """
    queryset = Product.objects.filter(is_active=True).order_by('id')
    serializer_class = ProductSerializer

    def post(self, request, *args, **kwargs):
        sub_category = request.data.get("sub-category")
        category = request.data.get("category")

        sub_category_obj = SubCategory.objects.filter(id=sub_category).first()
        if sub_category_obj:
            sub_category_obj.category = Category.objects.filter(id=category).first()
            sub_category_obj.save()
            Product.objects.create(title=request.data.get("product-title"), sub_category=sub_category_obj)

            return Response(self.serializer_class(self.get_queryset(), many=True).data)
        else:
            return Response({"status": False, "message": "Sub category is mandatory!"}, status=400)


