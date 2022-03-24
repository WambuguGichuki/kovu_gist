from django.shortcuts import render,redirect
from django.urls import reverse_lazy


from .models import Product,OrderItem,Order
from .forms import ProductForm,OrderItemFormset,OrderForm,OrderItemForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from django.forms import inlineformset_factory
from django.db import transaction


class CreateProduct(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "orders/create-product.html"
    success_url = reverse_lazy('orders:product_list')



class ProductList(ListView):
    model = Product
    template_name = "orders/product_list.html"
    context_object_name = "products"


def createorder(request):
    form = OrderItemForm()
    fields = request.GET.get('fields')
    # print(fields)

    # if request.method == "POST":
    #     if form.is_valid():
    #         form.save()
    #         return redirect("order_list")


    context = {"form":form,"order":OrderForm}

    return render(request,"orders/create-order.html",context)




def create_item_form(request):
    context = {"form":OrderItemForm()}

    form = request.GET.get('forms')
    print(form)


    return render(request,"orders/partials/new-items.html",context)



# class OrderCreate(CreateView):
#     model = Order
#     fields = ['customer_name','customer_phone','address','location','extra_details']
#     template_name = "orders/create-order.html"
#     success_url = reverse_lazy('orders:order_list')

#     def get_context_data(self, **kwargs):
#         data =  super(OrderCreate,self).get_context_data(**kwargs)
#         if self.request.POST:
#             data['items'] = OrderItemFormset(self.request.POST)
#         else:
#             data['items'] = OrderItemFormset()
#         return data

#     def form_valid(self, form):
#         context = self.get_context_data()
#         items = context['items']

#         with transaction.atomic():
#             self.object = form.save()

#             if items.is_valid():
#                 items.instance = self.object
#                 items.save()

#         return super(OrderCreate,self).form_valid(form)




class OrderDetail(DetailView):
    model = Order
    template_name = "orders/view-order.html"



class OrderList(ListView):
    model = Order
    template_name = "orders/order-list.html"
    context_object_name = 'orders'






