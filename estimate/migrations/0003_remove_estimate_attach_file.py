# Generated by Django 3.0.8 on 2020-09-16 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estimate', '0002_auto_20200916_2059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estimate',
            name='attach_file',
        ),
    ]