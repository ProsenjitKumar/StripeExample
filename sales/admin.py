from django.contrib import admin
from sales.models import Sale, Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'created', 'available', 'stock', 'image']
    list_editable = ['image', 'price']


class SaleAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Sale._meta.fields]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Sale, SaleAdmin)