# Generated by Django 3.1.7 on 2021-04-21 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_commentsss_reply_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentsss',
            name='pr_id',
            field=models.IntegerField(blank=True),
        ),
    ]
