# Generated by Django 3.1 on 2020-09-30 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=200)),
                ('billingStreet', models.TextField(default='')),
                ('billingCity', models.TextField(default='')),
                ('billingState', models.TextField(default='')),
                ('billingZipcode', models.TextField(default='')),
                ('shippingStreet', models.TextField(default='')),
                ('shippingCity', models.TextField(default='')),
                ('shippingState', models.TextField(default='')),
                ('shippingZipcode', models.TextField(default='')),
                ('gst_treatment', models.CharField(default='', max_length=200)),
                ('place_of_supply', models.CharField(default='', max_length=200)),
                ('invoice', models.CharField(default='', max_length=200)),
                ('order_no', models.CharField(default='', max_length=200)),
                ('invoice_date', models.CharField(default='', max_length=30)),
                ('terms', models.CharField(default='', max_length=100)),
                ('due_date', models.CharField(default='', max_length=30)),
                ('sales_person', models.CharField(default='', max_length=100)),
                ('sub_total', models.FloatField(default=0.0)),
                ('cgst', models.FloatField(default=0.0)),
                ('sgst', models.FloatField(default=0.0)),
                ('igst', models.FloatField(default=0.0)),
                ('discount', models.FloatField(default=0.0)),
                ('adjustments', models.FloatField(default=0.0)),
                ('round_off', models.FloatField(default=0.0)),
                ('total', models.FloatField(default=0.0)),
                ('customer_notes', models.TextField(default=0.0)),
                ('terms_condition', models.TextField(default=0.0)),
                ('organisation', models.CharField(default=' ', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice_transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_details', models.CharField(default='', max_length=250)),
                ('quantity', models.IntegerField(default=1.0)),
                ('rate', models.FloatField(default=0.0)),
                ('tax', models.CharField(default='', max_length=100)),
                ('amount', models.FloatField(default=0.0)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchaseitem.invoice')),
            ],
        ),
    ]