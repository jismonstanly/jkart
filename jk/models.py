from django.db import models

# Create your models here.
class Registration(models.Model):
 First_name = models.CharField(max_length=200)
 Last_name = models.CharField(max_length=200)
 Username = models.CharField(max_length=200)
 Password = models.CharField(max_length=200)

class Product(models.Model):
 Product_name=models.CharField(max_length=200)
 Product_price=models.IntegerField()
 Product_offer=models.IntegerField()
 Product_image = models.ImageField(upload_to='media')
 Product_category = models.CharField(max_length=100)
