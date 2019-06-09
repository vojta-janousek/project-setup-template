from django.urls import path

from products.views import (product_list, product_detail, manufacturer_detail,
                            manufacturer_list)
# from products.views import ProductListView, ProductDetailView


urlpatterns = [
    path('products/', product_list, name='product-list'),
    path('products/<int:pk>/', product_detail, name='product-detail'),
    # path('', ProductListView.as_view(), name='product_list'),
    # path('products/<int:pk>/', ProductDetailView.as_view(),
    #      name='product_detail'),
    path('manufacturers/', manufacturer_list, name='manufacturer-list'),
    path('manufacturers/<int:pk>/', manufacturer_detail,
         name='manufacturer-detail'),
]
