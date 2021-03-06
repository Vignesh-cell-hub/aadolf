# Generated by Django 3.1 on 2020-09-01 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primarycontact', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=200)),
                ('display_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('work_phone_no', models.CharField(max_length=15)),
                ('mobile_phone_no', models.CharField(max_length=15)),
                ('website', models.CharField(max_length=200)),
                ('gst_treatment', models.CharField(max_length=200)),
                ('source_of_supply', models.CharField(max_length=200)),
                ('currency', models.CharField(max_length=200)),
                ('opening_balance', models.DecimalField(decimal_places=2, max_digits=19)),
                ('payment_terms', models.CharField(max_length=200)),
                ('tds', models.CharField(max_length=200)),
                ('facebook', models.CharField(max_length=200)),
                ('twitter', models.CharField(max_length=200)),
                ('billing_attention', models.CharField(max_length=200)),
                ('billing_country', models.CharField(max_length=200)),
                ('billing_address', models.CharField(max_length=200)),
                ('billing_city', models.CharField(max_length=200)),
                ('billing_state', models.CharField(max_length=200)),
                ('billing_zipcode', models.CharField(max_length=15)),
                ('billing_phone', models.CharField(max_length=15)),
                ('billing_fax', models.CharField(max_length=15)),
                ('shipping_attention', models.CharField(max_length=200)),
                ('shipping_country', models.CharField(max_length=200)),
                ('shipping_address', models.CharField(max_length=200)),
                ('shipping_city', models.CharField(max_length=200)),
                ('shipping_state', models.CharField(max_length=200)),
                ('shipping_zipcode', models.CharField(max_length=15)),
                ('shipping_phone', models.CharField(max_length=15)),
                ('shipping_fax', models.CharField(max_length=15)),
            ],
        ),
    ]
