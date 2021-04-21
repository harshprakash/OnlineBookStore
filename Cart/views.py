from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Cart,BookOrder
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
#from django.conf import settings
from Bookstore import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .models import Order, ProductInOrder, Cart
from User.form import UserCreationForm


import logging

logger = logging.getLogger(__name__)
#getting order list
@login_required
def orders(request):
    
    order = Order.objects.filter(user=request.user)
    order_qs = ProductInOrder.objects.filter(order__in=order)
    

    
    context = {
       
        'order_qs' : order_qs,
        
    }
    return render(request, "Cart/order.html", context)
    
    
#fuction for add cart 
@login_required
def add_to_cart(request,book_id):
    book = get_object_or_404(Book, pk=book_id)
    cart,created = Cart.objects.get_or_create(user=request.user, active=True)
    cart.add_to_cart(book_id)
    return redirect('cart')     
#function for remove cart
@login_required
def remove_from_cart(request, book_id):
    if request.user.is_authenticated:
        try:
            book = Book.objects.get(pk = book_id)
        except ObjectDoesNotExist:
            pass 
        else:
            cart = Cart.objects.get(user = request.user, active = True)
            cart.remove_from_cart(book_id)
        return redirect('cart')
    else:
        return redirect('home')
# cartlist functionality
@login_required
def cart(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user, active=True)
        #relative_news = News.objects.filter(tag__id__in=news.tag.all())
        orders = BookOrder.objects.filter(cart__in=cart)
        total=0
        count=0
        for order in orders:
            total += (order.book.price * order.quantity)
            count += order.quantity
        context = {
            'cart': orders,
            'total': total,
            'count': count,
        }
        return render(request, 'Cart/cart.html', context)
    else:
        return redirect('home')


import razorpay
razorpay_client = razorpay.Client(auth=(settings.razorpay_id, settings.razorpay_account_id))

from .models import Order, ProductInOrder, Cart
# payment functionality
@login_required
def payment(request):
    if request.method == "POST":
        try:
            cart = Cart.objects.get(user = request.user)
            products_in_cart = BookOrder.objects.filter(cart = cart)
            print(products_in_cart)
            final_price = 0
            if(len(products_in_cart)>0):
                order = Order.objects.create(user = request.user, total_amount = 0)
                # order.save()
                for product in products_in_cart:
                    product_in_order = ProductInOrder.objects.create(order = order, product = product.book, quantity = product.quantity, price = product.book.price)
                    final_price = final_price + (product.book.price * product.quantity)
            else:
                return HttpResponse("No product in cart")
        except:
            return HttpResponse("No Book in cart")

        order.total_amount = final_price
        order.save()

        order_currency = 'INR'

        callback_url = 'http://'+ str(get_current_site(request))+"/handlerequest/"
        print(callback_url)
        notes = {'order-type': "basic order from the website", 'key':'value'}
        razorpay_order = razorpay_client.order.create(dict(amount=final_price*100, currency=order_currency, notes = notes, receipt=order.order_id, payment_capture='0'))
        print(razorpay_order['id'])
        order.razorpay_order_id = razorpay_order['id']
        order.save()
        
        return render(request, 'payment/paymentsummery.html', {'order':order, 'order_id': razorpay_order['id'], 'orderId':order.order_id, 'final_price':final_price, 'razorpay_merchant_id':settings.razorpay_id, 'callback_url':callback_url})
    else:
        return HttpResponse("505 Not Found") 


@csrf_exempt
def handlerequest(request):
    if request.method == "POST":
        try:
            payment_id = request.POST.get('razorpay_payment_id', '')
            order_id = request.POST.get('razorpay_order_id','')
            signature = request.POST.get('razorpay_signature','')
            params_dict = { 
            'razorpay_order_id': order_id, 
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
            }
            try:
                order_db = Order.objects.get(razorpay_order_id=order_id)
            except:
                return HttpResponse("505 Not Found")
            order_db.razorpay_payment_id = payment_id
            order_db.razorpay_signature = signature
            order_db.save()
            result = razorpay_client.utility.verify_payment_signature(params_dict)
            if result==None:
                amount = order_db.total_amount * 100   #we have to pass in paisa
                try:
                    razorpay_client.payment.capture(payment_id, amount)
                    order_db.payment_status = 1
                    order_db.save()
                    return render(request, 'payment/paymentsuccess.html',{'id':order_db.id})
                except:
                    order_db.payment_status = 2
                    order_db.save()
                    return render(request, 'payment/paymentfailed.html')
            else:
                order_db.payment_status = 2
                order_db.save()
                return render(request, 'payment/paymentfailed.html')
        except:
            return HttpResponse("505 not found")
# cancel order functionalitty
@login_required
def delete_order(request,id):

    orderid=Order.objects.get(id=id)

    orderid.delete()
    
    return render(request, 'Cart/deleteorder.html')
    
    

   
   
        

    
    

