from django.contrib import admin
from .models import Product
from .models import Category,Costomer,Order


# Register your models here.
class AdminCategory(admin.ModelAdmin):
    list_display = ['id','name']
admin.site.register(Category,AdminCategory)
class AdminProduct(admin.ModelAdmin):
    list_display = ['id','name','price','category','description']
admin.site.register(Product,AdminProduct)

class AdminCostomer(admin.ModelAdmin):
    list_display = ['id','fullname','phone','email','password']
admin.site.register(Costomer,AdminCostomer)

class AdminOrder(admin.ModelAdmin):
    list_display = ['id','product','customer','price','date']
    list_filter = ['date']
    list_editable = ['price']
    search_fields =['custome','product','date']
admin.site.register(Order,AdminOrder)

