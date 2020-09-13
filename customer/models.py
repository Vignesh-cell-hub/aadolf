from django.db import models


# Create your models here.
class Customer(models.Model):

    customer_type=models.CharField(max_length=200)
    primarycontact=models.CharField(max_length=200,default="Mr")
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    company_name=models.CharField(max_length=200)
    display_name=models.CharField(max_length=200)
    email=models.EmailField()
    work_phone_no=models.CharField(max_length=15)
    mobile_phone_no=models.CharField(max_length=15)
    website=models.CharField(max_length=200) 

    gst_treatment=models.CharField(max_length=200)
    place_of_supply=models.CharField(max_length=200)
    tax_prefrence=models.CharField(max_length=200)
    currency=models.CharField(max_length=200)
    opening_balance=models.DecimalField(max_digits=19,decimal_places=2)
    payment_terms=models.CharField(max_length=200)
    enable_portal=models.BooleanField(default=False)
    portal_language=models.CharField(max_length=200)
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

    def __str__(self):
     return self.company_name

