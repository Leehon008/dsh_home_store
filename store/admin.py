from django.contrib import admin

from store.models.revenue import Revenue
from .models.product import Products
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name','last_name','phone','email']

class AdminOrder(admin.ModelAdmin):
    list_display = ['product','customer','quantity','price', 'status','date']

class AdminRevenue(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'order','company']

# Register your models here.
admin.site.register(Products,AdminProduct)
admin.site.register(Category)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Order,AdminOrder)
admin.site.register(Revenue,AdminRevenue)


# username = leehon, email = honye.lewism@gmail.com, password = password
