from django.contrib import admin
from .models.product import ProductModel
from .models.category import CategoryModel
from .models.customer import Customer
from .models.orders import Order
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display=['category', 'price', 'title']

class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']


admin.site.register(ProductModel,ProductAdmin)
admin.site.register(CategoryModel,CategoryAdmin)
admin.site.register(Customer)
admin.site.register(Order)
#StoreZoneAdmin admin123