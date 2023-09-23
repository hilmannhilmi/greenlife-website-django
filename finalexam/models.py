from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class useraccounts(models.Model):
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    datecreated = models.DateField()
    email = models.CharField(max_length=50)
    buyerseller = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class userprofiles(models.Model):
    name = models.ForeignKey(useraccounts, on_delete=models.CASCADE)
    location = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class products(models.Model):
    name = models.CharField(max_length=100)
    dateadded = models.DateField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

class orders(models.Model):
    orderid = models.CharField(max_length=20)
    datecreated = models.DateField()
    shippinglocation = models.CharField(max_length=1000)

    def __str__(self):
        return f"Order ID: {self.orderid}, Shipping Location: {self.shippinglocation}"



