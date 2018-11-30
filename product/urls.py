from django.conf.urls import url

from product.views import CategoryListAPIView, SubCategoryListAPIView, ProductListCreateAPIView


urlpatterns = [

    url(r'^category/', CategoryListAPIView.as_view(), name="category-list"),
    url(r'^sub-category/', SubCategoryListAPIView.as_view(), name="sub-category-list"),
    url(r'^product/', ProductListCreateAPIView.as_view(), name="sub-category-list"),
]
