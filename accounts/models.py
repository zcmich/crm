from sre_constants import CATEGORY
from telnetlib import STATUS
from unicodedata import category
from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

# The __str__ method in Python represents the class objects as a string – it can be used for classes.
#  The __str__ method should be defined in a way that is easy to read and outputs all the members of the class.
    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY = (
                ('Indoor','Indoor'),
                ('Outdoor','Outdoor'),
           )

    name = models.CharField(max_length=200,null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200,choices=CATEGORY)
    description = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

class Order(models.Model):
    STATUS = (
                ('Pending', 'Pending'),
                ('Out for delivery', 'Out for delivery'),
                ('Delivered','Delivered')
             )
    # customer =
    # product =
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS )

