from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=7,decimal_places=2)

    def __str__(self):
        return self.name





class Order(models.Model):
    customer_name = models.CharField(max_length=200)
    customer_phone = models.CharField(max_length=200)
    address = models.CharField(max_length=400,null=True,blank = True)
    location = models.URLField(max_length=1000)
    extra_details = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
       ordering =  ['-updated','-created']

    def __str__(self):
        return str(self.id)

    @property
    def total_order(self):

        orderitems = OrderItem.objects.filter(order_id = self.id)
        sum = 0 
        for orderitem in orderitems:
            sum = (sum + orderitem.price)
        return sum

    @property
    def total_qty(self):
        orderitems = OrderItem.objects.filter(order_id = self.id)
        totalquantity = 0 
        for orderitem in orderitems:
            totalquantity = (totalquantity + orderitem.quantity)
        return totalquantity




class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1, blank=True,null=True)

    @property
    def price(self):
        return self.quantity * self.product.price

    def __str__(self):
        return str(self.order)

    
