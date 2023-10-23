from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin category class"""
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Admin product class"""
    list_display = ['title', 'author', 'slug', 'price', 'in_stock', 'created', 'is_active']
    list_filter = ['in_stock', 'is_active']
    prepopulated_fields = {'slug': ('title',)}
