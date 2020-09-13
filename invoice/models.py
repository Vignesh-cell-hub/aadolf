from django.db import models

# Create your models here.
class Invoice(models.Model):
    
    customer_name = models.CharField(max_length=200)
    billingAddress = models.TextField()
    shippingAddress = models.TextField()
    gst_treatment = models.CharField(max_length=200)
    place_of_supply = models.CharField(max_length=200)
    invoice = models.CharField(max_length=200)
    order_no = models.CharField(max_length=200)
    invoice_date = models.CharField(max_length=30)
    terms = models.CharField(max_length=100)
    due_date = models.CharField(max_length=30)
    sales_person = models.CharField(max_length=100)
    
    item_details = models.CharField(max_length=250,default='')
    quantity = models.FloatField(default=1.00)
    rate = models.FloatField(default=0.00)
    tax = models.CharField(max_length=100,default='')
    amount = models.FloatField(default=0.00)

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
    attach_file = models.FileField(upload_to='file',default='')

