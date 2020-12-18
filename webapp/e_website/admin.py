from django.contrib import admin
from .models import product,seller,order,buyer
# Register your models here.
admin.site.register(product)
admin.site.register(seller)
admin.site.register(order)
admin.site.register(buyer)