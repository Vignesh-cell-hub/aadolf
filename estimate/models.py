from django.db import models

# Create your models here.
class Estimate(models.Model):
    estimate_date = models.CharField(max_length=50)
    estimate_number = models.CharField(max_length=100)
    ref_number = models.CharField(max_length=250)
    customer_name = models.CharField(max_length=200)
    estimate_status = models.CharField(max_length=100)
    estimate_amount = models.FloatField()