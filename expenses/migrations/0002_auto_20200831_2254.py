# Generated by Django 3.1 on 2020-08-31 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='expense_file',
            field=models.FileField(upload_to='file/'),
        ),
    ]
