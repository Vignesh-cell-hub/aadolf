from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Vendor(models.Model):
    
    primarycontact=models.CharField(max_length=200)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    company_name=models.CharField(max_length=200)
    display_name=models.CharField(max_length=200)
    email=models.EmailField()
    work_phone_no=models.CharField(max_length=15)
    mobile_phone_no=models.CharField(max_length=15)
    website=models.CharField(max_length=200) 

    gst_treatment=models.CharField(max_length=200)
    source_of_supply=models.CharField(max_length=200)
    currency=models.CharField(max_length=200)
    opening_balance=models.DecimalField(max_digits=19,decimal_places=2)
    payment_terms=models.CharField(max_length=200)
    tds=models.CharField(max_length=200)
    facebook=models.CharField(max_length=200)
    twitter=models.CharField(max_length=200)

    billing_attention=models.CharField(max_length=200)
    billing_country=models.CharField(max_length=200)
    billing_address=models.CharField(max_length=200)
    billing_city=models.CharField(max_length=200)
    billing_state=models.CharField(max_length=200)
    billing_zipcode=models.CharField(max_length=15)
    billing_phone=models.CharField(max_length=15)
    billing_fax=models.CharField(max_length=15)

    shipping_attention =models.CharField(max_length=200)
    shipping_country =models.CharField(max_length=200)
    shipping_address =models.CharField(max_length=200)
    shipping_city =models.CharField(max_length=200)
    shipping_state =models.CharField(max_length=200)
    shipping_zipcode =models.CharField(max_length=15)
    shipping_phone =models.CharField(max_length=15)
    shipping_fax =models.CharField(max_length=15)
    organisation = models.CharField(max_length=200, default="")
