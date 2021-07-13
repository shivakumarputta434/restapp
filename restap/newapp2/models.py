from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.
currentDT = datetime.now()
class Emptable(models.Model):
    name=models.CharField(max_length=255,unique=True)
    age=models.IntegerField(default=0,blank=False)

class Category(models.Model):
    category=models.CharField(max_length=255)

class Color(models.Model):
    color=models.CharField(max_length=255)

class Product(models.Model):
    name=models.CharField(max_length=255)
    price=models.IntegerField(default=0)
    product_color=models.ForeignKey(Color,on_delete=models.CASCADE,related_name="product_color")
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product_category")
    releasedate=models.DateTimeField(default=timezone.now)
    featured=models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Company(models.Model):
    linkedin_url=models.CharField(max_length=250)
    retrieval_date=models.DateTimeField(default=datetime.now())
    linkedin_user=models.CharField(blank=True,max_length=250)

class Area(models.Model):
    area=models.CharField(max_length=250)
    areapin = models.IntegerField(default=0)
    areacolor=models.OneToOneField(Color,on_delete=models.CASCADE,related_name='areacolor')


class Houses(models.Model):
    housename=models.CharField(max_length=250)
    housecolor=models.ManyToManyField(Color)



status_choice=(
        ('process','In Process'),
        ('shipped','Shipped'),
        ('delivered','Delivered'),
    )
class CartOrder(models.Model):
    total_amt=models.FloatField()
    paid_status=models.BooleanField(default=False)
    order_dt=models.DateTimeField(auto_now_add=True)
    order_status=models.CharField(choices=status_choice,default='process',max_length=150)
