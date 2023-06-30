from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields specific to the Restaurant model

class Table(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    number = models.IntegerField()
    capacity = models.IntegerField()
    # Add other fields specific to the Table model

class Reservation(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    customer = models.CharField(max_length=100)
    date = models.DateField()
    # Add other fields specific to the Reservation model

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    # Add other fields specific to the Customer model
