from django.db import models
from django.urls import reverse
# from django.contrib.auth.models import AbstractUser

# Create your models here.

class Products(models.Model):
    name=models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.CharField(max_length=2500)


class UserModel(models.Model):
    username=models.CharField(max_length=25)
    password=models.CharField(max_length=200,blank=False)
    email=models.EmailField(max_length=200,unique=True,null=True, blank=False)


class BookData(models.Model):
    book_name = models.CharField(max_length=100, blank=False, null=False)
    book_author = models.CharField(max_length=100, blank=False, null=False)
    book_description = models.TextField(blank=False, null=False)
    book_price = models.DecimalField(max_digits=8, decimal_places=2)
    book_image = models.ImageField(
        upload_to='book_images/', blank=True, null=True)

    def __str__(self):
        return self.book_name
    
 
