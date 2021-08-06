# Generated by Django 3.2.6 on 2021-08-05 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_auto_20210804_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.IntegerField(default=0),
        ),
    ]