# Generated by Django 3.1.7 on 2021-04-10 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_addproducts_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addproducts',
            name='dicount_price',
        ),
        migrations.AddField(
            model_name='addproducts',
            name='dicount_percentage',
            field=models.CharField(blank=True, default=True, max_length=100),
        ),
        migrations.AddField(
            model_name='addproducts',
            name='discount_price',
            field=models.IntegerField(default=0),
        ),
    ]
