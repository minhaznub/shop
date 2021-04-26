from django.contrib import admin
from .models import Category,Product,Buyer,Product_Instences

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Buyer)
admin.site.register(Product_Instences)
