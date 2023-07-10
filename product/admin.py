from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(TopMenu)
admin.site.register(SubMenu)
admin.site.register(Products)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Cart)
admin.site.register(Wishlist)
admin.site.register(CouponCodeUsage)
admin.site.register(CouponCode)
admin.site.register(Order)
admin.site.register(Shade)
admin.site.register(Specification)
admin.site.register(Reviews)
admin.site.register(Gallery)
admin.site.register(NewsLetter)

class MapPriceListAdmin(admin.ModelAdmin):
    list_display = ('product', 'shade', 'specification', 'mrp')
admin.site.register(MapPriceList, MapPriceListAdmin)