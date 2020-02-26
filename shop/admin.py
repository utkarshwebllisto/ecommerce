from django.contrib import admin

from shop.models import (Product,
	                        Costumer,
	                        )

admin.site.register(Product)
admin.site.register(Costumer)