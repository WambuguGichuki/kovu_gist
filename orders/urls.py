from django.urls import path
from  . import views

urlpatterns = [
    
    path('products/',views.ProductList.as_view(),name = 'product_list'),
    path('products/create',views.CreateProduct.as_view(),name = 'create_product'),
    



    path('orders/',views.OrderList.as_view(),name = 'order_list'),
    path('orders/<int:pk>', views.OrderDetail.as_view(), name='order_details'),
    path('orders/create/', views.createorder, name='order_create'),


]