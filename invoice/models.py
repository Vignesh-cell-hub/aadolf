from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Invoice(models.Model):
    customer_name = models.CharField(max_length=200)
    billingStreet = models.TextField(default="")
    billingCity= models.TextField(default="")
    billingState = models.TextField(default="")
    billingZipcode = models.TextField(default="")
    shippingStreet = models.TextField(default="")
    shippingCity = models.TextField(default="")
    shippingState = models.TextField(default="")
    shippingZipcode = models.TextField(default="")
    gst_treatment = models.CharField(max_length=200,default="")
    place_of_supply = models.CharField(max_length=200,default="")
    invoice = models.CharField(max_length=200,default="")
    order_no = models.CharField(max_length=200,default="")
    invoice_date = models.CharField(max_length=30,default="")
    terms = models.CharField(max_length=100,default="")
    due_date = models.CharField(max_length=30,default="")
    sales_person = models.CharField(max_length=100,default="")

    sub_total = models.FloatField(default=0.00)
    cgst = models.FloatField(default=0.00)
    sgst = models.FloatField(default=0.00)
    igst = models.FloatField(default=0.00)
    discount = models.FloatField(default=0.00)
    adjustments = models.FloatField(default=0.00)
    round_off = models.FloatField(default=0.00)
    total = models.FloatField(default=0.00)

    customer_notes = models.TextField(default=0.00)
    terms_condition = models.TextField(default=0.00)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.invoice


class Invoice_transaction(models.Model):
    item_details = models.CharField(max_length=250, default='')
    quantity = models.IntegerField(default=1.00)
    rate = models.FloatField(default=0.00)
    tax = models.CharField(max_length=100, default='')
    amount = models.FloatField(default=0.00)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)