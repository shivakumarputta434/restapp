from django.contrib import admin
from .models import Emptable,Category,Color,Product,Company,Area,Houses,CartOrder

# Register your models here.

admin.site.register(Emptable)
admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Product)
admin.site.register(Company)
admin.site.register(Area)
admin.site.register(Houses)

class CartOrderAdmin(admin.ModelAdmin):
    list_display = ('id','total_amt','paid_status','order_dt','order_status')
admin.site.register(CartOrder,CartOrderAdmin)