from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Cart,BookOrder
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.contrib.auth.decorators import login_required
#from .forms import ReviewForm
#from store import signals
#import logging

#logger = logging.getLogger(__name__)

@login_required
def add_to_cart(self,request, *args, **kwargs):
    book_id = self.kwargs.get('pk')
    if request.user.is_authenticated():
        try:
            book = Book.objects.get(pk=book_id)
        except ObjectDoesNotExist:
            pass
        else:
            try:
                cart = Cart.objects.get(user=request.user, active=True)
            except ObjectDoesNotExist:
                cart = Cart.objects.create(
                    user = request.user
                )
                cart.save()
            cart.add_to_cart(book_id)
        return redirect('home')
    else:
        return redirect('home')

@login_required
def remove_from_cart(request, book_id):
    if request.user.is_authenticated():
        try:
            book = Book.objects.get(pk=book_id)
        except ObjectDoesNotExist:
            pass
        else:
            cart = Cart.objects.get(user=request.user, active=True)
            cart.remove_from_cart(book_id)
        return redirect('cart')
    else:
        return redirect('home')

@login_required
def cart(request):
    if request.user.is_authenticated():
        cart = Cart.objects.filter(user=request.user, active=True)
        orders = BookOrder.objects.filter(cart=cart)
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
        return render(request, 'cart/cart.html', context)
    else:
        return redirect('home')