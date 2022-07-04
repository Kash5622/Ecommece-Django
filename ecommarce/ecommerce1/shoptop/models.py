from django.db import models
import datetime
from django.utils.timezone import now

# Create your models here.


class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=20)
    category = models.CharField(max_length=15, default="")
    subcategory = models.CharField(max_length=15, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    stock=models.IntegerField(default=0)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name


class contact_us(models.Model):
    contact_us_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    uname = models.CharField(max_length=50)
    eaddress = models.CharField(max_length=50)
    tarea = models.CharField(max_length=500)

    def __str__(self):
        return self.eaddress


class order(models.Model):
    order_id=models.AutoField(primary_key=True)
    order_details=models.CharField(max_length=5000)
    total_amount=models.CharField(max_length=70)
    fname=models.CharField(max_length=70)
    lname=models.CharField(max_length=70)
    pnumber=models.CharField(max_length=70)
    address=models.CharField(max_length=500)
    email=models.CharField(max_length=70)
    state=models.CharField(max_length=70)
    zip=models.CharField(max_length=70)
    date=models.DateField(default=now)

    def __str__(self):
        return str(self.order_id)