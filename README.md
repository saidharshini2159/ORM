# Ex02 Django ORM Web Application
## Date: 14.10.2026

## AIM
To develop a Django Application to store and retrieve data from a Vehicle Service Database platform using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM
```
models.py
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

admin.py
from django.contrib import admin
from .models import Blinkit
class BlinkitAdmin(admin.ModelAdmin):
    list_display=["Product_no", "Product_name","User_name","Cost","Quantity","Discount","Address"]

admin.site.register(Blinkit,BlinkitAdmin)
```


## OUTPUT
![alt text](<Screenshot 2026-10-14 002409.png>)


## RESULT
Thus the program for creating Online Food Delivery Database using ORM hass been executed successfully
