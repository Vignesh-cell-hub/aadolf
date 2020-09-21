# Generated by Django 3.0.8 on 2020-09-21 08:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('estimate', '0005_auto_20200918_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='estimate',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]