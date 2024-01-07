from django.contrib import admin

# Register your models here.
from store.models import Category,Products,Order,Customer


class Store(admin.ModelAdmin):
    pass


admin.site.register(Category, Store)
admin.site.register(Order, Store)
admin.site.register(Customer, Store)
admin.site.register(Products, Store)


