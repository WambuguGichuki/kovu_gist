from django.urls import path
from  . import views

app_name = "orders"

urlpatterns = [
    
    path('products/',views.ProductList.as_view(),name = 'product-list'),
    path('products/create',views.CreateProduct.as_view(),name = 'create-product'),
    
    path('orders/create-item/',views.create_item,name = 'item-create'),


    path('orders/',views.OrderList.as_view(),name = 'order-list'),
    path('orders/<int:pk>', views.OrderDetail.as_view(), name="order-details"),
    path('orders/create/', views.CreateOrder.as_view(), name="order-create"),


]