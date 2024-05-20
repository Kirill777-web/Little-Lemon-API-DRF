from django.contrib import admin
from .models import Category, MenuItem, Cart, Order, OrderItem


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'featured', 'category']


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'delivery_crew', 'status', 'total', 'date')
    list_filter = ('status', 'date')
    search_fields = ('user__username', 'delivery_crew__username')


# Register your models here.
admin.site.register(Category)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Cart)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
