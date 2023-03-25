from django.contrib import admin

from .models import Product, Review


class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('product', 'rating', 'author', 'text')
    list_filter = ['created_at', 'author']

class ProductAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('name', 'category', 'description', 'image')
    list_filter = ['id', 'name']


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
