# Generated by Django 3.2.6 on 2021-08-04 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Product_name',
            new_name='product_name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Product_price',
            new_name='product_price',
        ),
    ]
