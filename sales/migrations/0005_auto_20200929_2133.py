# Generated by Django 3.0.8 on 2020-09-29 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_auto_20200929_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='organisation',
            field=models.CharField(default=' ', max_length=200),
        ),
    ]
