from django.contrib import admin

# Register your models here.
from .models import Cart,BookOrder
admin.site.register(Cart)
admin.site.register(BookOrder)