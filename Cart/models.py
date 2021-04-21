from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from Book.models import Book
#from __future__ import unicode_literals
#from django.utils.encoding import python_2_unicode_compatible

#Creation of database for Cart functionality
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    
    class Meta:
        db_table ="Cart"
    
    def __unicode__(self):
        return '%s %s' % (self.book_name, self.cart_id.user)    
    #updating databases for adding 
    def add_to_cart(self, book_id):
        book = Book.objects.get(pk=book_id)
        try:
            preexistting_order = BookOrder.objects.get(book=book, cart=self)
            preexistting_order.quantity +=1
            preexistting_order.save()
        except BookOrder.DoesNotExist:
            new_order = BookOrder.objects.create(
                book = book,
                cart = self,
                quantity = 1
            )
            new_order.save()


     #removing book  from database 
    def remove_from_cart(self, book_id):
        book = Book.objects.get(pk=book_id)
        try:
            preexistting_order = BookOrder.objects.get(book=book, cart=self)
            if preexistting_order.quantity > 1:
                preexistting_order.quantity -=1
                preexistting_order.save()
            else:
                preexistting_order.delete()
        except BookOrder.DoesNotExist:
            pass
    


class BookOrder(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    

    def __unicode__(self):
        return '%s %s' % (self.book_id.book_name, self.cart_id.user)     
    class Meta:
        db_table = "BookOrder"

    
# creating order status and payment status in databases
class Order(models.Model):
    status_choices = (
        (1, 'Not Packed'),
        (2, 'Ready For Shipment'),
        (3, 'Shipped'),
        (4, 'Delivered')
    )
    payment_status_choices = (
        (1, 'SUCCESS'),
        (2, 'FAILURE' ),
        (3, 'PENDING'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices = status_choices, default=1)

    total_amount = models.IntegerField()
    payment_status = models.IntegerField(choices = payment_status_choices, default=3)
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True, default=None) 
    datetime_of_payment = models.DateTimeField(default=timezone.now)
    # related to razorpay
    razorpay_order_id = models.CharField(max_length=500, null=True, blank=True)
    razorpay_payment_id = models.CharField(max_length=500, null=True, blank=True)
    razorpay_signature = models.CharField(max_length=500, null=True, blank=True)
    

    def save(self, *args, **kwargs):
        if self.order_id is None and self.datetime_of_payment and self.id:
            self.order_id = self.datetime_of_payment.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.user.email + " " + str(self.id)
    
    def get_absolute_url(self):
        return reverse('home', kwargs={'pk':self.pk})
    

    class Meta:
        db_table = "Order"
    

class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    product = models.ForeignKey(Book, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.IntegerField()

    








    
    # expiry_after_verified



# class Category(models.Model):
#     category_name = models.CharField(max_length=1000)

# class Subcategory(models.Model):
#     subcategory_name = models.CharField(max_length=1000)
#     category = models.ForeignKey(Category, on_delete = models.CASCADE)











