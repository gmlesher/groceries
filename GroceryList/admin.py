from django.contrib import admin
from django.contrib.admin import AdminSite
from GroceryList.API.models import *
# Register your models here.

AdminSite.site_header = 'Grocery List'

admin.register(
    GroceryItem,
    GroceryList
)(admin.ModelAdmin)

# @admin.register(GroceryList)
#
# @admin.register(GroceryItem)
# class GroceryItemAdmin(admin.ModelAdmin):
#     list_display = ('name','description', 'quantity','unit_of_measurement','sku_size',
#                     'brand','mfg_date','exp_date','price', 'currency')
