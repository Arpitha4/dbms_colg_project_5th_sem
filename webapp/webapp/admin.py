from django.contrib import admin
from .models import product,seller,buyer,cart,orders,address
# Register your models here.

admin.site.register(product)
admin.site.register(seller)
admin.site.register(buyer)
admin.site.register(cart)
admin.site.register(orders)
admin.site.register(address)