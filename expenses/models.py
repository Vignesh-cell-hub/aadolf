from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Expenses(models.Model):
    expense_date = models.CharField(max_length=20)
    expense_account = models.CharField(max_length=100)
    expense_type = models.CharField(max_length=50)
    expense_sac = models.CharField(max_length=200)
    expense_amount = models.FloatField()
    expense_paid = models.CharField(max_length=200)
    expense_vendor = models.CharField(max_length=200)
    expense_gst = models.CharField(max_length=200)
    expense_destination = models.CharField(max_length=200)
    expense_rev_charge = models.BooleanField()
    expense_tax = models.CharField(max_length=100)
    expense_invoice = models.CharField(max_length=100)
    expense_notes = models.TextField()
    customer_name = models.CharField(max_length=250)
    expense_file = models.FileField(upload_to="file/")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)