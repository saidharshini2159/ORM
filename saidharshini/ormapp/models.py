from django.db import models
from django.contrib import admin
class Blinkit(models.Model):
    Product_no=models.IntegerField(primary_key=True)
    Product_name=models.IntegerField(max_length=10)
    User_name=models.IntegerField(max_length=10)
    Cost=models.FloatField()
    Quantity=models.IntegerField()
    Discount=models.IntegerField()
    Address=models.TextField()
class Blinkitadmin(admin.ModelAdmin):
    list_display=["product_no", "Product_name","User_name","Cost","Quantity","Discount","Address"]

