from django.contrib import admin

# Register your models here.
from .models import Cart,BookOrder,Order,ProductInOrder
admin.site.register(Cart)
admin.site.register(BookOrder)
admin.site.register((Order,ProductInOrder))