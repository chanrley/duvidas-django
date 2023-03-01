from django.contrib import admin

from .models import Category, Item


admin.site.register(Category)


class OrderItem(admin.ModelAdmin):
    model = Item
    list_display = ['category', 'name', 'description', 'price', 'image', 'created_at']
    list_editable = ['name', 'description', 'price', 'image']
    readonly_fields = ['created_at']

admin.site.register(Item, OrderItem)
