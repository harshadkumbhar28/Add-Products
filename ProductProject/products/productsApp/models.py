from django.db import models


# Create your models here.

class products(models.Model):
    Product_Name = models.CharField(max_length=20)
    Price = models.FloatField()
    Description = models.CharField(max_length=200)



