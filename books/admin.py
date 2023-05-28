from django.contrib import admin

from .models import Product, Article, Panier

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
	fields = ("name", "price", "stock", "img", "description")


admin.site.register(Product, ProductAdmin)
admin.site.register(Article)
admin.site.register(Panier)
