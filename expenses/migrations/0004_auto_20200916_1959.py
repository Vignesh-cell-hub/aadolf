# Generated by Django 3.0.8 on 2020-09-16 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0003_merge_20200903_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='expense_amount',
            field=models.FloatField(),
        ),
    ]
