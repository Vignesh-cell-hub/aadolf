# Generated by Django 3.1 on 2020-08-29 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_auto_20200828_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='enable_portal',
            field=models.BooleanField(default=False),
        ),
    ]
