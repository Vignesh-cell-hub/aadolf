from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):

    customer_type=models.CharField(max_length=200,default="")
    primarycontact=models.CharField(max_length=200,default="Mr")
    first_name=models.CharField(max_length=200,default="")
    last_name=models.CharField(max_length=200,default="")
    company_name=models.CharField(max_length=200,default="")
    display_name=models.CharField(max_length=200,default="")
    email=models.EmailField(default="")
    work_phone_no=models.CharField(max_length=15,default="")
    mobile_phone_no=models.CharField(max_length=15,default="")
    website=models.CharField(max_length=200,default="")

    gst_treatment=models.CharField(max_length=200,default="")
    place_of_supply=models.CharField(max_length=200,default="")
    tax_prefrence=models.CharField(max_length=200,default="")
    currency=models.CharField(max_length=200,default="")
    opening_balance=models.DecimalField(max_digits=19,decimal_places=2,default=0.00)
    payment_terms=models.CharField(max_length=200,default="")
    enable_portal=models.BooleanField(default=False)
    portal_language=models.CharField(max_length=200,default="")
    facebook=models.CharField(max_length=200,default="")
    twitter=models.CharField(max_length=200,default="")

    billing_attention=models.CharField(max_length=200,default="")
    billing_country=models.CharField(max_length=200,default="")
    billing_address=models.CharField(max_length=200,default="")
    billing_city=models.CharField(max_length=200,default="")
    billing_state=models.CharField(max_length=200,default="")
    billing_zipcode=models.CharField(max_length=15,default="")
    billing_phone=models.CharField(max_length=15,default="")
    billing_fax=models.CharField(max_length=15,default="")

    shipping_attention =models.CharField(max_length=200,default="")
    shipping_country =models.CharField(max_length=200,default="")
    shipping_address =models.CharField(max_length=200,default="")
    shipping_city =models.CharField(max_length=200,default="")
    shipping_state =models.CharField(max_length=200,default="")
    shipping_zipcode =models.CharField(max_length=15,default="")
    shipping_phone =models.CharField(max_length=15,default="")
    shipping_fax =models.CharField(max_length=15,default="")

    organisation=models.CharField(max_length=200,default=" ")

    def __str__(self):
     return self.company_name

