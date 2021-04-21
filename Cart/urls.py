from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^add/(\d+)', views.add_to_cart, name='add_to_cart'),  
    url(r'^remove/(\d+)', views.remove_from_cart, name='remove_from_cart'),
    url(r'^cart/', views.cart, name='cart'),
    path('payment/', views.payment, name = 'payment'),
    path('handlerequest/', views.handlerequest, name = 'handlerequest'),
    path('myorder/', views.orders, name = 'myorder'),
    url(r'^delete_order/(\d+)', views.delete_order, name="delete_order")
    
    
    
]
