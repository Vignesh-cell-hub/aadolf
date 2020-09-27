from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Item(models.Model):
    item_type = models.CharField(max_length=200,null=True)
    name = models.CharField(max_length=200)
    units = models.CharField(max_length=200,null=True)
    hsncode = models.CharField(max_length=200,null=True)
    taxpreference = models.CharField(max_length=200,null=True)
    sellamount = models.CharField(max_length=200,null=True)
    salesacc = models.CharField(max_length=15,null=True)
    salesdes = models.CharField(max_length=15,null=True)
    puramount = models.CharField(max_length=200,null=True) 
    purchaseacc = models.CharField(max_length=200,null=True) 
    purchasedes = models.CharField(max_length=200,null=True) 
    intrastate = models.CharField(max_length=200,null=True)
    interstate = models.CharField(max_length=200,null=True)
    organisation = models.CharField(max_length=200, default=" ")
    