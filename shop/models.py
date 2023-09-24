#If anything we need to modified inside model need to migrate
from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length = 200)
    price =models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=100)
    description= models.TextField(default="Default text goes here.")
    image = models.CharField(max_length=300)
    
  #for changing the title name of the products inside Django data  
    def __str__(self):
        return self.title


class Order(models.Model):
    items = models.CharField(max_length=1000)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address= models.CharField(max_length=1000)
    address2=models.CharField(max_length=100)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    total = models.CharField(max_length=200)
