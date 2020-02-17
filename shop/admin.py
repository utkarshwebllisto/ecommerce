from django.contrib import admin

from shop.models import (Product,
	                        Addcart,
	                        Order)
# Register your models here.

admin.site.register(Product)
admin.site.register(Addcart)
admin.site.register(Order)