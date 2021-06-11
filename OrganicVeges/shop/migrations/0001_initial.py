# Generated by Django 3.1.7 on 2021-04-10 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addproducts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('section', models.CharField(blank=True, default=True, max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('dicount_price', models.IntegerField(default='')),
                ('value', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
