from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.username

class Product(models.Model):
    prod_name=models.CharField(max_length=20)
    qty=models.IntegerField()
    reg_time=models.DateField()

    def __str__(self):
        return self.prod_name