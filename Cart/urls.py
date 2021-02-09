from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
    
urlpatterns = [
    url('cart/', views.cart, name='cart'),
    url('addCart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    url('removeCart/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    
]
