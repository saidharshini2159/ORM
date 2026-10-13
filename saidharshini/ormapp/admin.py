from django.contrib import admin
from .models import Blinkit
class BlinkitAdmin(admin.ModelAdmin):
    list_display=["Product_no", "Product_name","User_name","Cost","Quantity","Discount","Address"]

admin.site.register(Blinkit,BlinkitAdmin)
