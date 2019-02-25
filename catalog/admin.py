from django.contrib import admin
from catalog.models import Product, Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'created', 'modified']
    search_fields = ['name', 'slug', 'category__name']
    list_filter = ['created', 'modified']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'modified']
    search_fields = ['name', 'slug']
    list_filter = ['created', 'modified']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)