
from django.contrib import admin
from django.urls import path,include
# from kovu.orders.views import createorder

from orders.views import (
    create_item_form
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(('orders.urls','orders'),namespace ='orders')),

    path('htmx/itemform',create_item_form,name = "form-item"),

    
]
