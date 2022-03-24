from winreg import QueryInfoKey
from django.forms import ModelForm,inlineformset_factory
from .models import Product,Order,OrderItem
from django import forms

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemForm(ModelForm):
    class Meta:
        model = OrderItem
        fields = ['product','quantity']

        
OrderItemFormset = inlineformset_factory(Order,OrderItem,form = OrderItemForm)


