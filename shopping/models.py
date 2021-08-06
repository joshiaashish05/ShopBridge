from django.db import models

# Create your models here.

class Product(models.Model):
    product_name=models.CharField(max_length=50,default="")
    product_price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300,default="")
    image=models.ImageField(upload_to='shop/images',default="")

    def __str__(self):
        return self.product_name