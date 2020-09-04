from django.contrib import admin
from .models import Products,offer


class offerAdmin(admin.ModelAdmin):
    list_display = ('code','discount')

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock')

admin.site.register(offer,offerAdmin)
admin.site.register(Products,ProductsAdmin)
