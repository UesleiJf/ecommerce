from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Product, Category

admin.site.register(Category)
admin.site.register(Product)
