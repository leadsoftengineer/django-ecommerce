#KYIV MEDIA 22.11.2019
from django.urls import path
from .views import (product_detail_view,product_create_view,product_initial_data,dynamic_lookup_view,product_delete_view,product_list_view)

urlpatterns = [
path('create/', product_create_view, name='create'),
path('product/', product_detail_view, name='product-detail'),
path('products/<int:my_id>/',dynamic_lookup_view, name='product-dynamic-detail'),
path('products/<int:id>/delete/', product_delete_view, name='product-delete'),
path('products/', product_list_view, name='product-list')
]