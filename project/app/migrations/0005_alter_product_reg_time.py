# Generated by Django 4.2 on 2023-06-20 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='reg_time',
            field=models.DateField(),
        ),
    ]
