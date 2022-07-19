from django.contrib import admin
from .models import Product,Offer


class ProductAdmin(admin.ModelAdmin):
    list_display=('item','price','stock')

class OfferAdmin(admin.ModelAdmin):
    list_display=('code','offer')

admin.site.register(Product,ProductAdmin)
admin.site.register(Offer,OfferAdmin)

# Register your models here.
