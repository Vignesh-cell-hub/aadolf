from django.db import models

# Create your models here.

class Estimate(models.Model):
    customer_name = models.CharField(max_length=200)
    billingStreet = models.TextField(default="")
    billingCity = models.TextField(default="")
    billingState = models.TextField(default="")
    billingZipcode = models.TextField(default="")
    shippingStreet = models.TextField(default="")
    shippingCity = models.TextField(default="")
    shippingState = models.TextField(default="")
    shippingZipcode = models.TextField(default="")
    gst_treatment = models.CharField(max_length=200,default="")
    place_of_supply = models.CharField(max_length=200,default="")
    estimate = models.CharField(max_length=200,default="")
    reference = models.CharField(max_length=200,default="")
    estimate_date =models.CharField(max_length=200,default="")
    expiry_date = models.CharField(max_length=200,default="")
    sales_person = models.CharField(max_length=200,default="")
    project_name =models.CharField(max_length=200,default="")

    sub_total = models.FloatField(default=0.00)
    cgst = models.FloatField(default=0.00)
    sgst = models.FloatField(default=0.00)
    igst = models.FloatField(default=0.00)
    discount = models.FloatField(default=0.00)
    adjustments = models.FloatField(default=0.00)
    round_off = models.FloatField(default=0.00)
    total = models.FloatField(default=0.00)

    customer_notes = models.TextField(default="")
    terms_condition = models.TextField(default="")

    def __str__(self):
        return self.estimate


class Estimate_transaction(models.Model):
    item_details = models.CharField(max_length=250, default='')
    quantity = models.IntegerField(default=1.00)
    rate = models.FloatField(default=0.00)
    tax = models.CharField(max_length=100, default='')
    amount = models.FloatField(default=0.00)
    invoice = models.ForeignKey(Estimate, on_delete=models.CASCADE)
