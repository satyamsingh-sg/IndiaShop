from django.contrib import admin
from .models import Product , Customers ,Cart ,Orderplaces,Token

# Register your models here.

admin.site.register(Product)
admin.site.register(Customers)
admin.site.register(Cart)
admin.site.register(Orderplaces)
admin.site.register(Token)