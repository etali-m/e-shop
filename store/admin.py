from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Tag)
admin.site.register(Product)
admin.site.register(Service)
admin.site.register(Provider)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingInfo)