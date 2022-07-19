from django.db import models



# Create your models here.
class Product(models.Model):
    item=models.CharField(max_length=255)
    price=models.FloatField()
    stock=models.IntegerField()
    image_url=models.CharField(max_length=2083)



class Offer(models.Model):
    code=models.CharField(max_length=10)
    discription=models.CharField(max_length=100)
    offer=models.FloatField()

